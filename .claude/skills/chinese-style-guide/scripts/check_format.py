#!/usr/bin/env python3
"""
中文写作排版格式检查工具
基于《中文写作排版风格指南》

用法:
    python check_format.py [选项] <file.md> [file2.md ...]

选项:
    --skip-tables     跳过 Markdown 表格行
    --warnings-only   只显示警告，不返回错误退出码

退出码:
    0 - 无错误
    1 - 发现格式错误
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Issue:
    """格式问题"""
    line_num: int
    column: int
    rule: str
    message: str
    context: str
    suggestion: str = ""
    level: str = "error"  # error 或 warning


class MarkdownParser:
    """Markdown 解析器，用于跳过代码块和表格"""

    def __init__(self, content: str, skip_tables: bool = False):
        self.lines = content.splitlines()
        self.in_code_block = False
        self.skip_tables = skip_tables

    def iter_lines(self) -> Iterator[tuple[int, str, bool]]:
        """迭代每一行，返回 (行号, 内容, 是否应跳过)"""
        for i, line in enumerate(self.lines, 1):
            # 检测围栏代码块 ```
            if line.strip().startswith("```"):
                self.in_code_block = not self.in_code_block
                yield (i, line, True)  # 代码块标记行也跳过
                continue

            # 跳过表格行
            if self.skip_tables and line.strip().startswith("|"):
                yield (i, line, True)
                continue

            yield (i, line, self.in_code_block)


class StyleChecker:
    """风格检查器"""

    # 中文字符范围
    CJK = r"\u4e00-\u9fff"
    CJK_PUNCT = r"。，！？：；""''《》（）、"

    def __init__(self, skip_tables: bool = False):
        self.issues: list[Issue] = []
        self.skip_tables = skip_tables

    def check_file(self, filepath: Path) -> list[Issue]:
        """检查单个文件"""
        self.issues = []
        content = filepath.read_text(encoding="utf-8")
        parser = MarkdownParser(content, skip_tables=self.skip_tables)

        for line_num, line, in_code_block in parser.iter_lines():
            if in_code_block:
                continue

            # 跳过行内代码的部分
            line_to_check = self._remove_inline_code(line)

            self._check_space_cn_en(line_num, line, line_to_check)
            self._check_space_cn_num(line_num, line, line_to_check)
            self._check_halfwidth_punctuation(line_num, line, line_to_check)
            self._check_straight_quotes(line_num, line, line_to_check)
            self._check_ellipsis(line_num, line, line_to_check)
            self._check_dash(line_num, line, line_to_check)
            self._check_fullwidth_colon_in_time(line_num, line, line_to_check)
            self._check_bracket_spaces(line_num, line, line_to_check)
            self._check_large_numbers(line_num, line, line_to_check)

        return self.issues

    def _remove_inline_code(self, line: str) -> str:
        """移除行内代码块，用空格替代"""
        # 处理 `` 双反引号
        line = re.sub(r"``[^`]+``", lambda m: " " * len(m.group()), line)
        # 处理 ` 单反引号
        line = re.sub(r"`[^`]+`", lambda m: " " * len(m.group()), line)
        return line

    def _check_space_cn_en(self, line_num: int, orig_line: str, line: str):
        """检查中英文之间是否有空格"""
        # 中文后紧跟英文
        pattern1 = re.compile(f"([{self.CJK}])([A-Za-z])")
        for m in pattern1.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 1,
                rule="missing-space-cn-en",
                message="中文与英文之间缺少空格",
                context=orig_line.strip(),
                suggestion=f"在 '{m.group(1)}' 和 '{m.group(2)}' 之间添加空格"
            ))

        # 英文后紧跟中文
        pattern2 = re.compile(f"([A-Za-z])([{self.CJK}])")
        for m in pattern2.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 1,
                rule="missing-space-cn-en",
                message="英文与中文之间缺少空格",
                context=orig_line.strip(),
                suggestion=f"在 '{m.group(1)}' 和 '{m.group(2)}' 之间添加空格"
            ))

    def _check_space_cn_num(self, line_num: int, orig_line: str, line: str):
        """检查中文与数字之间是否有空格"""
        # 中文后紧跟数字
        pattern1 = re.compile(f"([{self.CJK}])([0-9])")
        for m in pattern1.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 1,
                rule="missing-space-cn-num",
                message="中文与数字之间缺少空格",
                context=orig_line.strip(),
                suggestion=f"在 '{m.group(1)}' 和 '{m.group(2)}' 之间添加空格"
            ))

        # 数字后紧跟中文（排除"万""亿"等单位）
        pattern2 = re.compile(f"([0-9])([{self.CJK}])")
        for m in pattern2.finditer(line):
            # 排除数字后跟 万、亿、年、月、日、时、分、秒、点 等
            if m.group(2) in "万亿年月日时分秒点个百千":
                continue
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 1,
                rule="missing-space-cn-num",
                message="数字与中文之间缺少空格",
                context=orig_line.strip(),
                suggestion=f"在 '{m.group(1)}' 和 '{m.group(2)}' 之间添加空格"
            ))

    def _check_halfwidth_punctuation(self, line_num: int, orig_line: str, line: str):
        """检查中文句子中是否使用了半角标点"""
        # 中文后跟半角逗号
        pattern_comma = re.compile(f"([{self.CJK}]),")
        for m in pattern_comma.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 2,
                rule="halfwidth-punctuation",
                message="中文句子中使用了半角逗号",
                context=orig_line.strip(),
                suggestion="使用全角逗号 '，'"
            ))

        # 中文后跟半角句号（排除小数点和文件扩展名）
        pattern_period = re.compile(f"([{self.CJK}])\\.(?![0-9a-zA-Z])")
        for m in pattern_period.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 2,
                rule="halfwidth-punctuation",
                message="中文句子中使用了半角句号",
                context=orig_line.strip(),
                suggestion="使用全角句号 '。'"
            ))

        # 中文后跟半角问号
        pattern_question = re.compile(f"([{self.CJK}])\\?")
        for m in pattern_question.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 2,
                rule="halfwidth-punctuation",
                message="中文句子中使用了半角问号",
                context=orig_line.strip(),
                suggestion="使用全角问号 '？'"
            ))

        # 中文后跟半角感叹号
        pattern_exclaim = re.compile(f"([{self.CJK}])!")
        for m in pattern_exclaim.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 2,
                rule="halfwidth-punctuation",
                message="中文句子中使用了半角感叹号",
                context=orig_line.strip(),
                suggestion="使用全角感叹号 '！'"
            ))

        # 中文后跟半角冒号（排除时间格式如 9:05）
        pattern_colon = re.compile(f"([{self.CJK}]):(?![0-9])")
        for m in pattern_colon.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 2,
                rule="halfwidth-punctuation",
                message="中文句子中使用了半角冒号",
                context=orig_line.strip(),
                suggestion="使用全角冒号 '：'"
            ))

    def _check_straight_quotes(self, line_num: int, orig_line: str, line: str):
        """检查是否使用了直引号"""
        # 检测直双引号
        if '"' in line:
            # 排除 Markdown 链接 [text](url "title")
            line_no_links = re.sub(r'\[([^\]]*)\]\([^)]*\)', '', line)
            if '"' in line_no_links:
                col = line.find('"') + 1
                self.issues.append(Issue(
                    line_num=line_num,
                    column=col,
                    rule="straight-quotes",
                    message="使用了直引号",
                    context=orig_line.strip(),
                    suggestion="使用弯引号 '""'"
                ))

    def _check_ellipsis(self, line_num: int, orig_line: str, line: str):
        """检查省略号格式"""
        # 检测三个连续的点
        pattern = re.compile(r"\.{3}")
        for m in pattern.finditer(line):
            # 检查是否在中文上下文中
            before = line[:m.start()]
            after = line[m.end():]
            if re.search(f"[{self.CJK}]", before) or re.search(f"[{self.CJK}]", after):
                self.issues.append(Issue(
                    line_num=line_num,
                    column=m.start() + 1,
                    rule="wrong-ellipsis",
                    message="中文上下文中使用了 '...' 作为省略号",
                    context=orig_line.strip(),
                    suggestion="使用中文省略号 '……'"
                ))

    def _check_dash(self, line_num: int, orig_line: str, line: str):
        """检查破折号格式"""
        # 检测两个连续的短横线
        pattern = re.compile(r"(?<!-)--(?!-)")
        for m in pattern.finditer(line):
            # 检查是否在中文上下文中
            before = line[:m.start()]
            after = line[m.end():]
            if re.search(f"[{self.CJK}]", before) or re.search(f"[{self.CJK}]", after):
                self.issues.append(Issue(
                    line_num=line_num,
                    column=m.start() + 1,
                    rule="wrong-dash",
                    message="中文上下文中使用了 '--' 作为破折号",
                    context=orig_line.strip(),
                    suggestion="使用中文破折号 '——'"
                ))

    def _check_fullwidth_colon_in_time(self, line_num: int, orig_line: str, line: str):
        """检查时间格式中是否误用全角冒号"""
        # 检测数字：数字的模式
        pattern = re.compile(r"[0-9]+：[0-9]+")
        for m in pattern.finditer(line):
            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 1,
                rule="fullwidth-colon-in-time",
                message="时间格式中使用了全角冒号",
                context=orig_line.strip(),
                suggestion="时间应使用半角冒号 ':'"
            ))

    def _check_bracket_spaces(self, line_num: int, orig_line: str, line: str):
        """检查书名号和括号内的多余空格"""
        # 书名号内开头有空格
        if re.search(r"《\s", line):
            self.issues.append(Issue(
                line_num=line_num,
                column=line.find("《") + 1,
                rule="extra-space-in-brackets",
                message="书名号开头有多余空格",
                context=orig_line.strip(),
                suggestion="删除 '《' 后的空格"
            ))

        # 书名号内结尾有空格
        if re.search(r"\s》", line):
            self.issues.append(Issue(
                line_num=line_num,
                column=line.find("》") + 1,
                rule="extra-space-in-brackets",
                message="书名号结尾有多余空格",
                context=orig_line.strip(),
                suggestion="删除 '》' 前的空格"
            ))

        # 全角括号内开头有空格
        if re.search(r"（\s", line):
            self.issues.append(Issue(
                line_num=line_num,
                column=line.find("（") + 1,
                rule="extra-space-in-brackets",
                message="全角括号开头有多余空格",
                context=orig_line.strip(),
                suggestion="删除 '（' 后的空格"
            ))

        # 全角括号内结尾有空格
        if re.search(r"\s）", line):
            self.issues.append(Issue(
                line_num=line_num,
                column=line.find("）") + 1,
                rule="extra-space-in-brackets",
                message="全角括号结尾有多余空格",
                context=orig_line.strip(),
                suggestion="删除 '）' 前的空格"
            ))

    def _check_large_numbers(self, line_num: int, orig_line: str, line: str):
        """检查大数字是否缺少千位分隔符"""
        # 检测 5 位及以上的连续数字（不含已有逗号的）
        pattern = re.compile(r"(?<![0-9,])[0-9]{5,}(?![0-9,])")
        for m in pattern.finditer(line):
            num = m.group()
            after = line[m.end():m.end()+1] if m.end() < len(line) else ""
            before = line[m.start()-1:m.start()] if m.start() > 0 else ""
            before_context = line[max(0, m.start()-10):m.start()]

            # 排除可能是 ID、版本号等
            if before in "-_./" or after in "-_./:":
                continue

            # 排除标准编号（如 GB/T 15834, GB 3100 等）
            if re.search(r"GB/?T?\s*$", before_context, re.IGNORECASE):
                continue

            # 排除 URL 中的数字
            if "http" in line or "://" in line:
                continue

            self.issues.append(Issue(
                line_num=line_num,
                column=m.start() + 1,
                rule="unformatted-large-number",
                message=f"大数字 '{num}' 缺少千位分隔符",
                context=orig_line.strip(),
                suggestion=f"使用千位分隔符: '{self._format_number(num)}'",
                level="warning"
            ))

    def _format_number(self, num_str: str) -> str:
        """格式化数字，添加千位分隔符"""
        return "{:,}".format(int(num_str))


def print_report(filepath: Path, issues: list[Issue]):
    """打印检查报告"""
    print(f"\n{'=' * 60}")
    print(f"文件: {filepath}")
    print(f"{'=' * 60}\n")

    if not issues:
        print("  未发现格式问题")
        return

    errors = [i for i in issues if i.level == "error"]
    warnings = [i for i in issues if i.level == "warning"]

    for issue in issues:
        level_mark = "错误" if issue.level == "error" else "警告"
        print(f"[{level_mark}] 第 {issue.line_num} 行, 列 {issue.column}: {issue.message}")
        print(f"  > {issue.context}")
        if issue.suggestion:
            print(f"  建议: {issue.suggestion}")
        print()

    print(f"总计: {len(errors)} 个错误, {len(warnings)} 个警告")


def main():
    # 解析命令行参数
    args = sys.argv[1:]
    skip_tables = False
    warnings_only = False
    files = []

    for arg in args:
        if arg == "--skip-tables":
            skip_tables = True
        elif arg == "--warnings-only":
            warnings_only = True
        elif arg.startswith("-"):
            print(f"未知选项: {arg}")
            print(__doc__)
            sys.exit(1)
        else:
            files.append(arg)

    if not files:
        print(__doc__)
        print("错误: 请指定要检查的文件")
        sys.exit(1)

    checker = StyleChecker(skip_tables=skip_tables)
    total_errors = 0
    total_warnings = 0

    for filepath_str in files:
        filepath = Path(filepath_str)
        if not filepath.exists():
            print(f"错误: 文件不存在: {filepath}")
            sys.exit(1)

        issues = checker.check_file(filepath)
        print_report(filepath, issues)

        errors = [i for i in issues if i.level == "error"]
        warnings = [i for i in issues if i.level == "warning"]
        total_errors += len(errors)
        total_warnings += len(warnings)

    print(f"\n总计: {total_errors} 个错误, {total_warnings} 个警告")

    if total_errors > 0 and not warnings_only:
        print("请修正后重试。")
        sys.exit(1)
    else:
        if total_errors == 0:
            print("所有文件检查通过！")
        sys.exit(0)


if __name__ == "__main__":
    main()

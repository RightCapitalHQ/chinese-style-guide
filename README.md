# 中文写作排版风格指南

本文对中文文章的中英文写作风格、用语、排版的风格作出规范和建议。

## 中文

### 汉字规范

1. 使用简体字，推荐遵守《[通用规范汉字表](https://zh.wikisource.org/wiki/通用规范汉字表)》。

### 用语

1. 使用中国大陆地区通行的词汇和惯用语，不使用港台地区词语。

   正确

   > 算法、参数、数组、回调

   错误

   > 演算法、引数、阵列、回呼

1. 不使用网络语言和网络流行语。

    错误

    > 喜大普奔、不明觉厉、囧、焱暒妏

1. 不使用带歧视性的、不雅的语言。

    错误

    > 屌丝、P 事

1. 使用简练直白的语言。

    正确

    > 我们认为人人生而平等。

    错误

    > 我们认为以下真理是不言而喻的：人人生而平等。

1. 避免错别字。

    正确

    > 登录、阈值、重启

    错误

    > 登陆、阀值、重起

### 翻译

1. 使用中国大陆地区的译法，不使用港台地区的译法。
1. 当一个英文单词在没有广为接受的汉译词语或者使用其汉译词语会产生歧义时，可以使用英文单词本身。

    正确

    > 在 debug 过程中， 我们发现当参数为 `null` 时，会触发另外一个 bug。

    错误

    > 在排障过程中， 我们发现当参数为 `空` 时，会触发另外一个故障。

1. 当一个英文缩写为人熟知并广为接受时，可以使用英文缩写而不使用其中文翻译。

    正确

    > RightCapital 的 CEO 拥有哥伦比亚大学的 MBA 学位。
    >
    > RightCapital 的首席执行官拥有哥伦比亚大学的工商管理硕士学位。

1. 当要表达一个英文词汇，其中文翻译尚未被广为接受或存在歧义时，可以把英文原文写在括号里作为注释。在一篇文章中，同一个词汇只在其第一次出现的地方添加注释。

    正确

    > 在常见的 HTTP 方法中，POST 和 PATCH 不是幂等（idempotent）的。
    >
    > 字符串字面量（string literal）以 `null` 字符结束。

### 中英文混排

1. 在中文文章标题、段落和句子中出现的英文单词、短语和句子，其拼写、用法和风格遵守本指南中的[英文](#英文)部分。
1. 中文句子独立出现的英文名词，无论是表达一个还是多个，都使用该名词的单数形式。

    正确

    > 这段代码中有好几个 bug。

    错误

    > 这段代码中有好几个 bugs。

### 排版格式

1. 不使用段首缩进（例如段落左空二字）。

### 空格

1. 汉字与英文，汉字与阿拉伯数字之间应添加一个空格。

    正确

    > 世界上有 10 种人，一种是懂二进制的，另一种是不懂的。

    错误

    > 世界上有10种人，一种是懂二进制的，另一种是不懂的。

1. 汉字标点与英文，汉字标点与阿拉伯数字之间不应该添加空格。

    正确

    > 在《The Hitchhiker’s Guide to the Galaxy》中，生命、宇宙以及一切的终极答案是 42。

    错误

    > 在《 The Hitchhiker’s Guide to the Galaxy 》中，生命、宇宙以及一切的终极答案是 42 。

1. 汉字与半角标点之间不添加空格。

    正确

    > 订阅的价格是 100 美元/月。

    错误

    > 订阅的价格是 150 美元 / 月。

1. 汉字中格式化的部分（比如加粗、斜体、颜色、上下角标、超链接等）和未格式化的部分之间不应使用空格。

    正确

    > PHP 是世界上**最好**的[语言](https://zh.wikipedia.org/zh-cn/编程语言)。

    错误

    > PHP 是世界上 **最好** 的 [语言](https://zh.wikipedia.org/zh-cn/编程语言)。

### 标点符号和排版符号

1. 中文标点符号的用法，原则上遵守 [GB/T 15834](https://github.com/Haixing-Hu/typesetting-standard/blob/master/数字文字/【GB:T%2015834-2011】标点符号用法.pdf)。
1. 中文句子中使用汉字标点符号。注意大部分汉字标点符号是全角（full width）的，但也有例外（如分隔号“/”），具体参考下表：

    | 标点符号 | 形式 | 字形  | Unicode  | 注释 |
    | ------- | --- |:----:| -------- | --- |
    | 句号     | | 。   | U+3002 IDEOGRAPHIC FULL STOP | 不使用 U+FF0E FULLWIDTH FULL STOP |
    | 逗号     | | ，   | U+FF0C FULLWIDTH COMMA | |
    | 顿号     | | 、   | U+3001 IDEOGRAPHIC COMMA | |
    | 感叹号   | | ！   | U+FF01 FULLWIDTH EXCLAMATION MARK | |
    | 问号     | | ？   | U+FF1F FULLWIDTH QUESTION MARK | |
    | 冒号     | | ：   | U+FF1A FULLWIDTH COLON | |
    | 分号     | | ；   | U+FF1B FULLWIDTH SEMICOLON | |
    | 引号  | 左 | “   | U+201C LEFT DOUBLE QUOTATION MARK | |
    |   | 右 | ”   | U+201D RIGHT DOUBLE QUOTATION MARK | |
    | 书名号  | 左 | 《   | U+300A LEFT DOUBLE ANGLE BRACKET | |
    |   | 右 | 》   | U+300B RIGHT DOUBLE ANGLE BRACKET | |
    | 括号   | 左 | （   | U+FF08 FULLWIDTH LEFT PARENTHESIS | |
    |    | 右 | ）   | U+FF09 FULLWIDTH RIGHT PARENTHESIS | |
    | 破折号   | | ——    | 两个 U+2014 EM DASH | 不使用 U+2E3A TWO-EM DASH |
    | 省略号   | | ……    | 两个 U+2026 HORIZONTAL ELLIPSIS | |
    | 分隔号   | | /    | U+002F SOLIDUS | 不使用 U+FF0F FULLWIDTH SOLIDUS |
    | 连接号 | 短横线 | -    | U+002D HYPHEN-MINUS | |
    |  | 一字线 | —    | U+2014 EM DASH | |
    |  | 波浪号 | ～   | U+FF5E FULLWIDTH TILDE | |

1. 中文段落中的句子中如果出现的英文语段，英文语段中标点符号应遵循本指南本指南中的[英文](#英文)部分。

    正确

    > RightCapital 的办公室文化是“Work smart, play hard, live well”。

    错误

    > RightCapital 的办公室文化是“Work smart，play hard，live well”。

1. 并列的词语之间如果是“或”的关系，可以使用分隔号“/”。
1. 并列词语之间应该使用顿号。

    正确

    > RightCapital 的技术部是由前端、后端、运维三个团队组成。

    错误

    > RightCapital 的技术部是由前端，后端，运维三个团队组成。

1. 并列词语之间，当最后两个词语之间如果使用“和”或者“或”这类连词，词语之间不应该仿照英文的牛津逗号使用顿号。

    正确

    > RightCapital 的技术部是由前端、后端和运维三个团队组成。

    错误

    > RightCapital 的技术部是由前端、后端、和运维三个团队组成。

1. 使用弯引号““””，不应使用直角引号“「」”。
1. 直角引号可以用于分割专有名词。

    正确

    > RightCapital 的内部 IT 系统是基于「零信任」原则构建。

1. 在中文句子中使用括号注释句中语段，如果括号中的内容和括号所修饰的内容都是英文，应使用半角括号，否则应使用全角括号。

    正确

    > RightCapital (a fintech company) 的手机应用（app）于近日发布。

    错误

    > RightCapital（a fintech company）的手机应用 (app) 于近日发布。

1. 中文句子中的出现的出版物名称，无论中文还是英文，都应该使用书名号“《》”。

    正确

    > 《三体》和《The Hitchhiker’s Guide to the Galaxy》都是值得一读的科幻小说。

    错误

    > 《三体》和 *The Hitchhiker’s Guide to the Galaxy* 都是值得一读的科幻小说。

1. 汉字的区间和范围应使用一字线“—”或者波浪号“～”。阿拉伯数字的范围参考本指南中的[英文](#英文)部分。

     正确

     > 北京—上海的高铁最快仅需 4 小时 18 分。

     错误

     > 北京-上海的高铁最快仅需 4 小时 18 分。

1. 在分行列举中，如果并列各项不是完整句子时，除最后一项外，各项都应使用分号结尾；最后一条应使用句号结尾。

    正确

    > RightCapital 为每一位开发提供了<br>
        1. 一台 27 英寸 iMac；<br>
        2. 第二台 27 英寸 4K 显示器；<br>
        3. 无限量小食和饮料。

1. 在分行列举中，如果并列各项是完整句子时，每项都使用句号结尾。

    正确

    > RightCapital 的所有开发都应当<br>
        1. 写代码。<br>
        2. 注重团队协作。<br>
        3. 尊重彼此。

1. 使用半角百分号。

     正确

     > 在引入了新的优化之后，系统的性能得到了 15% 的提升。

1. 使用半角版本数学符号，包括负号“-”、加号“+”、减号“-”、乘号“*”、除号“/”等。

### 数字

1. 数字的用法原则上遵守 [GB/T 15835](http://www.moe.gov.cn/ewebeditor/uploadfile/2015/01/13/20150113091154536.pdf)。
1. 不超过 10 的数字推荐使用中文数字，10 和 10 以上的数字推荐使用阿拉伯数字。
1. 使用半角版本阿拉伯数字。
1. “万”“亿”中文单位可以使用阿拉伯数字，其它中文单位只能使用汉字数字。

    正确

    > 这个代码仓库有 300 万行代码。
    >
    > 这个代码仓库有三百行代码。

    错误

    > 这个代码仓库有 3 百万行代码。
    >
    > 这个代码仓库有 3 百行代码。

1. 中文句子中出现的阿拉伯数字时，如果数字是四位或者四位以上，应该使用半角逗号按千位分隔。

    正确

    > 这个代码仓库有 3,000,000 行代码。

    错误

    > 这个代码仓库有 3000000 行代码。
    >
    > 这个代码仓库有 300,0000 行代码。

### 电话号码

1. 座机号码应该在局号（电话号码的前 3 位或者 4 位）和最后 4 位号码之间使用短横线或者空格进行分隔。

    正确

    > 6123-4567
    >
    > 123 4567

    错误

    > 61234567
    >
    > 1234567

1. 座机号码当包含区号时，区号需添加长途冠码 0，区号和号码之间使用一个空格，区号可以使用括号。

    正确

    > 010 6123-4567
    >
    > (010) 6123-4567

    错误

    > 01061234567
    >
    > (010)6123-4567

1. 手机号应该按照 3-4-4 分组，使用短横线或空格分隔。

    正确

    > 139-1234-5678

    错误

    > 1391-234-5678
    >
    > (139) 1234-5678
    >
    > 13912345678

1. 400 或者 800 号码按照 3-3-4 分组，使用短横线或空格分隔。

    正确

    > 400-123-4567

    错误

    > (400) 123-4567
    >
    > 4001234567

1. 国际冠码和国际区号的使用参照本指南中的[英文](#英文)部分。

1. 座机号码当包含国际区号时，必须同时包含国内区号，且国际区号必须添加国际冠码，国内区号必须不添加长途冠码。

    正确

    > +86 10 6123-4567
    >
    > +86 (10) 6123-4567

    错误

    > +86 010 6123-4567

### 日期和时间

1. 日期和时间的用法原则上遵守 [GB/T 15835](http://www.moe.gov.cn/ewebeditor/uploadfile/2015/01/13/20150113091154536.pdf)。
1. 日期应按照年月日顺序书写。

    正确

    > 2020 年 3 月 31 日
    >
    > 2020-3-31
    >
    > 2020-03-31

    错误

    > 3 月 31 日 2020 年
    >
    > 3-31-2020
    >
    > 2020/3/31

1. 年份应该用 4 位数。

    正确

    > 2020 年 3 月 31 日
    >
    > 2020-3-31

    错误

    > 20 年 3 月 31 日
    >
    > 20-3-31

1. 使用汉字“月”“日”时，不编虚位（即1不编为01）。

    正确

    > 3 月 31 日

    错误

    > 03 月 31 日

1. 时间中的时、分、秒使用半角冒号“:”分隔。

    正确

    > 上午 9:05

    错误

    > 上午 9：05

1. 关于时间的其它规则参见本指南中的[英文](#英文)部分。

### 量和单位

1. 量和单位的用法原则上遵守 [GB 3100](https://github.com/Haixing-Hu/typesetting-standard/blob/master/量和单位/【GB%203100-1993】国际单位制及其应用.pdf)、[GB 3101](https://github.com/Haixing-Hu/typesetting-standard/blob/master/量和单位/【GB%203101-1993】有关量、单位和符号的一般原则.pdf) 和 GB 3102（全部）。
1. 量和单位的用法可以参考[《量和单位的名称、符号及书写规则》](https://github.com/Haixing-Hu/typesetting-standard/blob/master/量和单位/量和单位的名称、符号及书写规则.pdf)。

## 英文

### 基本规则

1. 英文段落和中文段落中的英文单词、短语和句子，其语法、用法和风格原则上遵守[《Chicago Manual of Style》](https://www.chicagomanualofstyle.org/home.html)。

### 拼写

1. 使用美式英语拼写。

    正确

    > Color, grey, center, canceled

    错误

    > Colour, gray, centre, cancelled

1. 商标和品牌名应该遵循其官方拼写。

    正确

    > RightCapital, App Store, AT&T, eBay, Yahoo!, Häagen-Dazs

    错误

    > Right Capital, AppStore, AT & T, Ebay, Yahoo, Haagen—Dazs

### 大小写

1. 商标和品牌名应该遵循其官方拼写风格使用大小写，即使位于段首也不对其首字母大写。

    正确

    > iPhone 在短短数年内就挑战了 BlackBerry 在企业市场中的地位。

    错误

    > Iphone 在短短数年内就挑战了 blackberry 在企业市场中的地位。

1. 文章的标题（title）、出版物名称（包括书籍、音乐和影视作品等）应该使用标题大小写（title case），而非句子大小写（sentence case）。
1. 章节的标题（heading）、表格和图表的标题、表格的表头应使用句子大小写。
1. 在条目列表中，当条目都是包含动词的完整句子时，所有条目的第一个单词的首字母都应该大写。

    正确

    > All RightCapital developers<br>
        1. Write code.<br>
        2. Work as a team.<br>
        3. Respect each other.

1. 避免使用全大写（all-caps）。

    错误

    > TALK IS CHEAP. Show me the code.

### 排版格式

1. 不使用段首缩进。
1. 出版物名称使用斜体。

    正确

    > *The Hitchhiker’s Guide to the Galaxy* is a comedy science fiction series created by Douglas Adams.

### 空格

1. 数字和单位之间通常使用空格，百分号“%”、温度单位（摄氏度“°C”、华氏度“°F”）、和角度单位（度“°”、分“′”、秒“″”）除外。

    正确

    > 5.0 cm, 45 kg, 32°C, 50%, 45°

    错误

    > 5.0cm, 45kg, 32 °C, 50 %, 45 °

1. 数字和倍数符号（multiples symbol）之间，倍数符号和单位之间都不使用空格。出于历史原因，cm、km、kg 等按照单位处理，而不按照带倍数符号的单位处理。

    正确

    > 128GB, 40Gb, 5GHz

    错误

    > 128 GB, 40 Gb, 5 GHz

### 标点符号和排印符号

1. 英文句子使用英文标点，不应使用汉字标点。英文标点应使用以下字符：

    | 标点符号 | 形式 | 字形  | Unicode  | 注释 |
    | ------- | --- |:----:| -------- | --- |
    | 撇号  |  | ’   | U+2019 RIGHT SINGLE QUOTATION MARK | 不使用 U+0027 APOSTROPHE |
    | 引号  | 左 | “   | U+201C LEFT DOUBLE QUOTATION MARK | 不使用 U+0022 QUOTATION MARK |
    |   | 右 | ”   | U+201D RIGHT DOUBLE QUOTATION MARK | 不使用 U+0022 QUOTATION MARK |
    | 省略号   | | ...  | 三个 U+002E FULL STOP | 不使用 U+2026 HORIZONTAL ELLIPSIS |
    | 连字符 | | - | U+002D HYPHEN-MINUS | |
    | En dash | | – | U+2013 EN DASH | |
    | Em dash | | — | U+2014 EM DASH | |

1. 英文句子中最后一个单词如果以点“.”结尾，则该句不再使用句号。

    正确

    > The company’s name is RightCapital Inc.
    >
    > There are apples, oranges, etcs.

    错误

    > The company’s name is RightCapital Inc..
    >
    > There are apples, oranges, etcs..

1. 括号的外侧需要保留一个空格。

    正确

    > RightCapital (a fintech company) is based in Shelton, Connecticut.

    错误

    > RightCapital(a fintech company)is based in Shelton, Connecticut.

1. 在三个或三个以上并列词组之间，在连词（例如“and”或者“or”）之前应该使用牛津逗号。

    正确

    > RightCapital’s engineering department consists of front-end, back-end, and DevOps teams.

    错误

    > RightCapital’s engineering department consists of front-end, back-end and DevOps teams.

1. 破折号应使用 em dash “—”，不能使用连字符（hyphen）“-”。破折号左右不要留空格，也不要连续使用两个 em dash “——”。

    正确

    > RightCapital’s web development teams—front-end and back-end—are working together to make it happen.

1. 表示区间时推荐使用 en dash “–”，不推荐使用连字符。

    正确

    > Financial Highlights for Fiscal Year 2018–2019

1. 在条目列表中，当条目都是短语或者分句时，除最后一项使用句号结尾外，其余各项使用逗号结尾。

    正确

    > Every RightCapital developer is offered<br>
        1. an 27-inch iMac,<br>
        2. a second 27-inch 4K screen, and<br>
        3. unlimited snacks and beverage.

1. 在条目列表中，当条目都是带动词的完整句子时，各项都应该用句号结尾。

    正确

    > All RightCapital developers<br>
        1. Write code.<br>
        2. Work as a team.<br>
        3. Respect each other.

1. 在文章正文中不建议使用 ampersand “&”，应该展开为“and”，但专有名词（例如品牌名）不受此限。

    正确

    > Abercrombie & Fitch is an American lifestyle retailer. It operates two other brands: Abercrombie Kids and Hollister Co.

    错误

    > Abercrombie and Fitch is an American lifestyle retailer. It operates two other brands: Abercrombie Kids & Hollister Co.

1. 商标符号使用“™”，注册商标符号使用“®”，版权符号使用“©”。

    正确

    > Copyright © RightCapital Inc. 2015–2020

    错误

    > Copyright (c) RightCapital Inc. 2015–2020

1. 脚标所注释的内容，在同一页面内，应该依次使用星号“*”、剑标“†”、和双剑标“‡”、分节符“§”、双竖线“||”、井号“#”，这些符号应该以上角标（superscript）形式出现在所注释的内容结尾处，与所注释的内容之间不使用空格。

    正确

    > RightCapital’s financial planning software, launched in 2015<sup>*</sup>, is top-rated<sup>†</sup>.

### 货币

1. 货币前缀和数字之间不使用空格。

    正确

    > $12.34
    >
    > US$1,234.56

    错误

    > $ 1,234.56
    >
    > US$ 1,234.56

1. 在财务/会计语境中，负数用括号（而不是负号）表示。货币符号置于括号之外。

    正确

    > $(12.34)

    错误

    > $-12.34

### 数字

1. 四位和四位以上的数字应使用逗号作为千位分隔符。

    正确

    > This repo has 3,000,000 lines of code.

    错误

    > This repo has 3000000 lines of code.
    >
    > This repo has 3.000.000 lines of code.

1. 序数（ordinal number）中的字母不应该以上角标出现。

    正确

    > 1st, 2nd, 3rd

    错误

    > 1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup>

### 电话号码

1. 区号可以使用括号，当使用括号时区号和 7 位的电话号码之间使用空格；区号不用括号时，用连字符和电话号码分隔。电话号码中的前 3 位中心局（central office）号和最后 4 位用连字符分隔。

    正确

    > (212) 123-4567
    >
    > 212-123-4567

    错误

    > (212)123-4567
    >
    > 212 123-4567
    >
    > 212 123 4567

1. 国际电话号码应使用加号“+”作为国际冠码（IDD prefix），国际冠码和国际区号之间不使用空格，国际区号和区号使用空格分隔。

    正确

    > +1 (212) 123-4567
    >
    > +1 212-123-4567

    错误

    > 011 (212) 123-4567
    >
    > +1(212) 123-4567
    >
    > +1-212-123-4567
    >
    > \+ 1 (212) 123-4567

### 日期和时间

1. 使用美式风格的日期，按照月日年顺序书写。

    正确

    > Sunday, January 31, 2021
    >
    > January 31, 2021
    >
    > Jan. 31, 2021
    >
    > 1/31/2021
    >
    > 01/31/2021

    错误

    > Sunday, 31 January, 2021
    >
    > 31 January 2021
    >
    > 31/1/2021
    >
    > 2021-1-31

1. 日期中的日不使用序数。

    正确

    > January 31

    错误

    > January 31st

1. 12 小时制的时间，a.m./p.m. 使用小写；其中的点“.”可以省略；时间和 a.m./p.m. 之间使用一个空格。

    正确

    > 9:30 a.m., 9:30 am

    错误

    > 9:30a.m., 9:30am 9:30 A.M., 9:30 AM

1. 午夜和正午 12 点应分别使用“12:00 midnight”和“12:00 noon”，“midnight”和“noon”使用小写。

    正确

    > 12:00 midnight, 12:00 noon

    错误

    > 12:00 Midnight, 12:00 Noon
    >
    > 12:00 a.m., 12:00 p.m., 0:00 a.m., 0:00 p.m.

1. 12 小时制的时间，小时部分必须不编虚位，24 小时制的时间，小时部分必须使用虚位保持两位数字。分和秒的部分必须使用虚位保持两位数字。

    正确

    > 9:05 am, 09:05

    错误

    > 09:05 am, 9:05, 9:5 am

## 代码

1. 变量类型，数据库字段类型，类、方法、函数、变量的名字，字面量（literal），在句子中应该格式化为代码。

    正确

    > 这个函数会把 `$id` 参数保存到数据库中一个 `TINYINT UNSIGNED` 类型的字段中。所以当其取值超出 `255` 的时候，这个函数会抛出 `InvalidArgumentException` 异常。

1. 字符串字面量（string literal）当格式化为代码时，如果在句中不引起歧义，可以不加引号。

    正确

    > 当 `$color` 参数为 `transparent` 的时候，函数会抛出 `InvalidArgumentException` 异常。
    >
    > 当 `$color` 参数为 `"transparent"` 的时候，函数会抛出 `InvalidArgumentException` 异常。

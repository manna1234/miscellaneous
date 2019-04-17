# DBF文件格式说明

DBF文件是一种以二进制进行存储的表格数据文件，其文件内部有着严格的格式要求，具体由文件头和记录项组成。其中文件头中包括字段的相关信息。DBF文件的数据结构如下表所示：

------

<table>
   <tr>
      <td>组成</td>
      <td>内容</td>
      <td>位置（Byte）</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>文件头</td>
      <td>文件头定义</td>
      <td>0-31</td>
      <td>包括版本信息、更新时间、记录条数、文件头长度等</td>
   </tr>
   <tr>
      <td></td>
      <td>字段1定义</td>
      <td>32-64</td>
      <td>字段名称、类型、字段长度(Byte)、精度等</td>
   </tr>
   <tr>
      <td></td>
      <td>字段2定义</td>
      <td>65-97</td>
      <td>同上</td>
   </tr>
   <tr>
      <td></td>
      <td>……</td>
      <td></td>
      <td>同上</td>
   </tr>
   <tr>
      <td></td>
      <td>字段n定义</td>
      <td>-n*32+31</td>
      <td>同上</td>
   </tr>
   <tr>
      <td></td>
      <td>值为0x0D</td>
      <td>n*32+32</td>
      <td>表示终止字段定义</td>
   </tr>
   <tr>
      <td>表格记录数据</td>
      <td>第1行数据</td>
      <td>n*32+33-X</td>
      <td>表示第1行数据</td>
   </tr>
   <tr>
      <td></td>
      <td>第2行数据</td>
      <td></td>
      <td>表示第2行数据</td>
   </tr>
   <tr>
      <td></td>
      <td>……</td>
      <td></td>
      <td></td>
   </tr>
</table>





注意，在表格记录数据中每行数据具体占多长字节，这个由文件头中定义的字段数目以及字段长度来决定，如果该文件一共只有两个字段，其中第一个字段为数值，其长度为4，第二个字段为字符串，长度为50，则每一行数据占的字节长度为4+50=54，在读取数据时也是读取前4个为第一个字段对应的值，读取第5-54个为第二个字段对应的值。

另外，为便于理解表格与下面内容的关系，特说明字段即是指表格中的列，记录指表格中的行数据，DBF按行数据方式来存储，即在文件头中定义了列数、列的名称、列的数据类型、列长度等等，然后在后面的记录数据中插入每行数据。



------

文件头中格式及说明如下：

<table>
   <tr>
      <td>位置</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>0</td>
      <td>1个字节</td>
      <td>	
表示当前的版本信息：
<LI>0x02 FoxBASE
<LI>0x03 FoxBASE+/Dbase III plus, no memo
<LI>0x30 Visual FoxPro
<LI>0x31 Visual FoxPro, autoincrement enabled
<LI>0x43 dBASE IV SQL table files, no memo
<LI>0x63 dBASE IV SQL system files, no memo
<LI>0x83 FoxBASE+/dBASE III PLUS, with memo
<LI>0x8B dBASE IV with memo
<LI>0xCB dBASE IV SQL table files, with memo
<LI>0xF5 FoxPro 2.x (or earlier) with memo
<LI>0xFB FoxBASE
</td>
   </tr>
   <tr>
      <td>1－3</td>
      <td>3个字节</td>
      <td>表示最近的更新日期，按照YYMMDD格式，以1900年为起始，即第一个字节表示文件最后保存时的年份-1900，第二个字节的值为保存时的月，第三个字节的值为保存时的日。</td>
   </tr>
   <tr>
      <td>4－7</td>
      <td>Int32</td>
      <td>文件中的记录条数，即表格的行数。</td>
   </tr>
   <tr>
      <td>8－9</td>
      <td>Int16</td>
      <td>文件头中的字节数，在此之后的字节为表格记录数据</td>
   </tr>
   <tr>
      <td>10－11</td>
      <td>Int16</td>
      <td>一条记录中的字节长度，即每行数据所占的长度</td>
   </tr>
   <tr>
      <td>12－13</td>
      <td>2个字节</td>
      <td>保留字节，用于以后添加新的说明性信息时使用，这里用0来填写。</td>
   </tr>
   <tr>
      <td>14</td>
      <td>1个字节</td>
      <td>表示未完成的操作。</td>
   </tr>
   <tr>
      <td>15</td>
      <td>1个字节</td>
      <td>dBASE IV编密码标记。</td>
   </tr>
   <tr>
      <td>16－27</td>
      <td>12个字节</td>
      <td>保留字节，用于多用户处理时使用。</td>
   </tr>
   <tr>
      <td>28</td>
      <td>1个字节</td>
      <td>DBF文件的MDX标识。在创建一个DBF 表时 ，如果使用了MDX 格式的索引文件，那么 DBF 表的表头中的这个字节就自动被设置了一个标志，当你下次试图重新打开这个DBF表的时候，数据引擎会自动识别这个标志，如果此标志为真，则数据引擎将试图打开相应的MDX 文件。</td>
   </tr>
   <tr>
      <td>29</td>
      <td>1个字节</td>
      <td>页码标记.</td>
   </tr>
   <tr>
      <td>30－31</td>
      <td>2个字节</td>
      <td>保留字节，用于以后添加新的说明性信息时使用，这里用0来填写。</td>
   </tr>
   <tr>
      <td>32－N</td>
      <td>（x*32）个字节</td>
      <td>这段长度由表格中的列数（即字段数，Field Count）决定，每个字段的长度为32，如果有x列，则占用的长度为x*32，这每32个字节里面又按其规定包含了每个字段的名称、类型等信息，具体见下面的表。</td>
   </tr>
   <tr>
      <td>N＋1</td>
      <td>1个字节</td>
      <td>作为字段定义的终止标识，值为0x0D。</td>
   </tr>
</table>

 

------

每个字段定义格式如下表，每个字段定义都用32个字节来完成：

 <table>
   <tr>
      <td>位置</td>
      <td>内容</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>0－10</td>
      <td>11个字节</td>
      <td>字段的名称，是ASCII码值。</td>
   </tr>
   <tr>
      <td>11</td>
      <td>1个字节</td>
      <td>字段的数据类型，为ASCII码值。每个值对应不同的字段数据类型，如N表示数值，C表示字符串，关于具体的数据类型说明见下表。</td>
   </tr>
   <tr>
      <td>12－15</td>
      <td>4个字节</td>
      <td>保留字节，用于以后添加新的说明性信息时使用，默认为0。</td>
   </tr>
   <tr>
      <td>16</td>
      <td>1个字节</td>
      <td>字段的长度，表示该字段对应的值在后面的记录中所占的长度。</td>
   </tr>
   <tr>
      <td>17</td>
      <td>1个字节</td>
      <td>字段的精度。</td>
   </tr>
   <tr>
      <td>18－19</td>
      <td>2个字节</td>
      <td>保留字节，用于以后添加新的说明性信息时使用，默认为0。</td>
   </tr>
   <tr>
      <td>20</td>
      <td>1个字节</td>
      <td>工作区ID。</td>
   </tr>
   <tr>
      <td>21－31</td>
      <td>11个字节</td>
      <td>保留字节，用于以后添加新的说明性信息时使用，默认为0。</td>
   </tr>
</table>

------

字段数据类型：

<table>
   <tr>
      <td>代码</td>
      <td>数据类型</td>
      <td>允许输入的数据</td>
   </tr>
   <tr>
      <td>B</td>
      <td>二进制型</td>
      <td>各种字符。</td>
   </tr>
   <tr>
      <td>C</td>
      <td>字符型</td>
      <td>各种字符。</td>
   </tr>
   <tr>
      <td>D</td>
      <td>日期型</td>
      <td>用于区分年、月、日的数字和一个字符，内部存储按照YYYYMMDD格式。</td>
   </tr>
   <tr>
      <td>G</td>
      <td>(General or OLE)</td>
      <td>各种字符。</td>
   </tr>
   <tr>
      <td>N</td>
      <td>数值型(Numeric)</td>
      <td>- . 0 1 2 3 4 5 6 7 8 9</td>
   </tr>
   <tr>
      <td>L</td>
      <td>逻辑型（Logical）</td>
      <td>? Y y N n T t F f (? 表示没有初始化)。</td>
   </tr>
   <tr>
      <td>M</td>
      <td>(Memo)</td>
      <td>各种字符。</td>
   </tr>
</table>

------


# JvavSer

## 解题过程

### **下载解压得到：JvavSer.jar**

### **查看源码**

用`IDEA`新建项目，将`JvavSer.jar`放入`lib`文件夹下，将`lib`文件夹设为`库`

看到`Main`调用了`JvavSer`，`JvavSer`实现了`IJvavSer`，主要的题目逻辑就在`IJvavSer`的`launch`函数

```java
//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.probie.jvavser.Jvavser.Interface;

import com.probie.encryption.Encryption;
import com.probie.jvavser.Data.Data;
import java.io.PrintStream;
import java.util.Scanner;

public interface IJvavSer {
    default int launch(String[] args) {
        for(String welcomeMessage : Data.getWelcomeMessage()) {
            System.out.println(welcomeMessage);
        }

        System.out.printf("%s", Data.getInputFlagMessage());
        Scanner scanner = new Scanner(System.in);
        if (scanner.hasNext()) {
            String flag = scanner.next();
            if (Encryption.getInstance().isDebug()) {
                PrintStream var10000 = System.out;
                String var10001 = Data.getFlagMessage();
                var10000.println(var10001 + Data.getFLAG());

                try {
                    Thread.sleep(1000L);
                    return 0;
                } catch (InterruptedException interruptedException) {
                    throw new RuntimeException(interruptedException);
                }
            }

            if (flag.contains("{") && flag.contains("}")) {
                String format = flag.split("\\{")[0];
                if (format.toUpperCase().toLowerCase().equalsIgnoreCase("pkwsec")) {
                    Encryption.getInstance().getConfigFactory().getKeyConfig().getLocalDB().connect(ClassLoader.getSystemResourceAsStream("Key"));
                    Encryption.getInstance().getConfigFactory().getKeyConfig().getLocalDB().setIsAutoCommit(false);
                    flag = Encryption.getInstance().getEncrypterFactory().getMapEncrypter().encryptByMap(Encryption.getInstance().getEncoderFactory().getSerializeEncoder().encodeSerialize(Encryption.getInstance().getEncoderFactory().getBase64Encoder().encodeBase64(Encryption.getInstance().getEncoderFactory().getCaesarEncoder().encodeCaesar(Encryption.getInstance().getEncoderFactory().getXOEncoder().encodeXO(flag.substring(flag.indexOf("{") + 1, flag.lastIndexOf("}")))))));
                    if (flag.equals(Data.getC())) {
                        System.out.println(Data.getRightFlagMessage());

                        try {
                            Thread.sleep(1000L);
                            return 0;
                        } catch (InterruptedException interruptedException) {
                            throw new RuntimeException(interruptedException);
                        }
                    }
                }
            }
        }

        System.out.println(Data.getWrongFlagMessage());

        try {
            Thread.sleep(1000L);
            return 0;
        } catch (InterruptedException interruptedException) {
            throw new RuntimeException(interruptedException);
        }
    }
}
```

**分析**

- 这段代码先分析输入的`flag`是否含有`pkwsec`前缀，然后判断是否属于`pkswec{}`格式
- 然后将`flag`体的内容拿出来，依次进行
  - 亦或
  - 凯撒
  - Base64
  - 序列化
  - 自定义Map字符映射加密
- 然后得到密文与`c`作比较

我们得先求出`c`然后依次逆向

我们找一下`Data.getC()`的实现逻辑

```java
public static String getC() {
    try (LocalDB localDB = EasyDB.getInstance().getLocalDatabaseFactory().buildLocalDB()) {
        if (localDB.connect(ClassLoader.getSystemResourceAsStream("C"))) {
            localDB.setIsAutoCommit(false);
            setC(new com.probie.easydb.DataPacket.Data().deCode(localDB.get("c")).get("c").toString());
        }
    }
    return Data.C;
}
```

**分析**

- 可以看到这个方法的逻辑是先获取`C`文件中`c键`的值`c值`
- 然后将这个值反序列化为`Data`类的实例化对象
- 接着从这个`Data`类的实例化对象中取出`c键`的值返回

我们先查看我们需要的两个附件`Key`和`C`

### **查看附件**

查看`Key`文件

```shell
#A Local Database Of LocalDB Basic On Properties
#Fri Dec 19 00:07:29 CST 2025
caesar=114514
map=rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmD...
xor=k
```

查看`C`文件

```shell
#A Local Database Of LocalDB Basic On Properties
#Fri Dec 19 00:07:29 CST 2025
c=rO0ABXNyACFjb20ucHJvYmllLmVhc3lkYi5EYXRhUGFja...
```

**分析**

- 可以看到除了我们需要的`map`和`c`外，还有`凯撒偏移量114514`和`亦或字符k`
- 我们需要先尝试反序列化`c`得到`Data`，进而得到`concurrentHashMap`，最终得到密文`c`

### **逆向密文C**

**思路**

- 已知`JVM`的序列化机制只关注：`包路径`、`类名`、`修饰符`、`字段名称`等

  我们只需要写一个和`Data类`相似甚至相同的类来进行反序列化就可以取出密文`c`

  保险起见出题人甚至将题目所使用的`JDK版本`都在`Data`中直接告诉我们了

  ```java
  private final static String JDK_VERSION = "21.0.8";
  ```

  这个方法在这里也是可行的

- 不过转念一想有无捷径可走？既然我们需要一个和`Data类`相似甚至相同的类，那何不直接就用题目的`Data类`呢！还记得我们一开始已经将这个`jar`包作为了`lib`依赖了，那么我们可以调用它里面的方法来帮我们实现逆向！

**代码示例**

```java
// 模仿Data.getC()函数反序列化c并获取返回值c，略
```

**得到密文C：**

```shell
x&tXc|{cX!yI(=Z9(wKG(qb9bwyI(HW9(w#q(qb<E!yI(=y9(w#a(qb<y)yI(=,9(wKw(qb<y)yIOHy9(w#q(qb9$)yI(={9(wK](qb93!yIOHu9(w#H(qb9bwyIOHO9(wKx(qb9bqyI(=b9(wK](qb<y)yI(=O9(wK9(qb9$wyIOHR9(wKt(qb9S!yI(=y9(w#H(qb9$!yI(=u9(wKt(qb9$wyIOHR9(w#=(qb9$!yI(=O9(wKt(qb<KwyI(=y9(w#=(qb<ywyIOHb9(wKs(qb9$)yI(=O9(wK<(qb9$)yIOHR9(wKG(qb9$!yIOHZ9(w#=(qb<ywyIOHO9(wKs(qb<KwyIOHR\
```

### **逆向Flag**

**思路**

- 先反序列化map为HashMap类的实例化对象然后将键值对调，然后将密文通过map进行一次字符映射
- 接着将得到的输出反序列化一次
- 然后Base64解码操作一次
- 接着凯撒左移114514位一次
- 然后与`k`进行一次亦或操作

**代码示例**

```java
// 略
```

**得到Flag**

```shell
3718ad6bc71cfa7084df1a9258c165b086f0405be010e6eae37127b70ceaa3eb
```

### **得到：pkwsec{3718ad6bc71cfa7084df1a9258c165b086f0405be010e6eae37127b70ceaa3eb}**
# week-11

- 2023.01.30 ~ 2023.02.05

이번 주는 **정수론**에 대해서 알아보겠습니다.
문제는 다음과 같습니다.

## 🤓 mandatory part

- [x] [다음 소수](https://www.acmicpc.net/problem/4134)

문제에서 입력값의 범위를 정수 n(0 ≤ n ≤ 4*10^9) 로 주고 있습니다

이는 int 형 범위를 벗어나는 수가 들어올 수 있음을 뜻합니다

- int 의 경우 -2,147,483,648~ 2,147,483,647 까지 표현
- unsigned int 는 0~4,294,967,295까지 표현

이에 더 큰 값이 들어올 경우를 생각해보다 BigInteger 에 대해 공부하게 되었습니다

## BigInteger

4byte 로 표현할 수 있는 범위를 넘어,

8byte 로 표현이 가능한 long 형이 있습니다

- long 형의 범위: -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807

해당 범위를 벗어나면 모두 0으로 출력됩니다

무한의 정수를 출력하고 싶다면? `BigInteger` 를 사용할 수 있습니다

- 선언

```java
import java.math.BigInteger;

BigInteger bigNumber = new BigInteger("10000");
```

BigInteger 은 String 입니다

그렇기에 BigInteger 내부의 숫자를 계산하기 위해서는 

BigInteger 클래스 내부에 있는 메서드를 사용해야 합니다

BigInteger 클래스에서 두가지의 메서드를 사용해봤습니다

- `isProbablePrime(certainty)`

숫자가 소수인지 판별합니다

인자는 확실성을 나타내는 certainty 입니다

만일 메소드가 true 를 반환한다면, 이는 소수인지 확인하고자 하는 정수가 소수일 확률이 1-(1/2)^certainty 의 확률을 넘는다는 의미입니다

보통 이 값이 10인 경우 확률이 0.9990234375 정도 되므로 웬만한 큰 수의 소수는 판별할 수 있습니다

더 높은 정확성을 위해 11 이상의 값을 넣는 경우 그만큼 메소드 수행 시간이 증가하므로 필요한 만큼만 설정하여 사용하면 됩니다

- `nextProbablePrime()`

다음 소수를 찾아줍니다


- [x] [Base Convension](https://www.acmicpc.net/problem/11576)

진법 변환을 돕는 메서드는 다음과 같습니다

## 10진법 to n진법

```java
int a = 25;

int BaseN_Number = Integer.toString(a, (int)N);
```


## n진법 to 10진법

```java
String a = "25";

int BaseN_Number = Integer.parseInt(a,(int)N);
```

해당 문제는 숫자를 자릿수로 구분하고 있으므로 이를 고려해야 합니다

로직에 Stack 자료구조를 활용했습니다

## Stack

- 선언

```java
Stack<Integer> stack = new Stack();
Stack<String> stack = new Stack<>();
```

- 메서드

    값 추가

    - add()
    - push()

    값 삭제

    - pop()
    - clear() // all
    
    가장 상단의 값을 가져오기

    - peak() // 값 제거 x

- [x] [최소공배수](https://www.acmicpc.net/problem/13241)

유클리드 호제법을 활용해 최대 공약수를 구한다

조건 = a > b
```c
int gcd(int a, int b)
{
    while (b > 0)
    {
        int tmp = a;
        a = b;
        b = tmp%b;
    }
    return a;
}
```

재귀를 활용
```c
int gcd(int a, int b)
{
    return b ? gcd(b, a%b) : a;
}
```

최대공약수를 활용해 최소 공배수를 구한다

```c
lcd = (a * b) / gcd;
```

- [x] [최대공약수](https://www.acmicpc.net/problem/1850)

엄청나게 많은 숫자가 입력될 경우 자료형의 범위를 먼저 생각해보고

이후 함정은 아닐까 생각해보자

1을 500000000000000000 번 쓰면 1천조에 해당한다

1로 변환하고 공약수를 구하는 것이 아닌,

먼저 공약수를 구하고 그 숫자만큼 1을 출력하면 되는 규칙이었다

이 문제를 통해 print()를 여러 번 호출할 경우 println() 한 번과 확연히 차이가 날 수 있음을 느꼈다


- [ ] [GCD 합](https://www.acmicpc.net/problem/9613)
- [ ] [수 복원하기](https://www.acmicpc.net/problem/2312)
- [ ] [관중석](https://www.acmicpc.net/problem/10166)
- [ ] [골드바흐의 추측](https://www.acmicpc.net/problem/6588)
- [ ] [소수상근수](https://www.acmicpc.net/problem/9421)
- [ ] [보이는 점의 개수](https://www.acmicpc.net/problem/2725)


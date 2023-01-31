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


- [ ] [Base Convension](https://www.acmicpc.net/problem/11576)
- [ ] [최소공배수](https://www.acmicpc.net/problem/13241)
- [ ] [최대공약수](https://www.acmicpc.net/problem/1850)
- [ ] [GCD 합](https://www.acmicpc.net/problem/9613)
- [ ] [수 복원하기](https://www.acmicpc.net/problem/2312)
- [ ] [관중석](https://www.acmicpc.net/problem/10166)
- [ ] [골드바흐의 추측](https://www.acmicpc.net/problem/6588)
- [ ] [소수상근수](https://www.acmicpc.net/problem/9421)
- [ ] [보이는 점의 개수](https://www.acmicpc.net/problem/2725)


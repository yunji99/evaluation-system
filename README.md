# 결과 평가 시스템

- 입력 데이터 형식: 예측 txt, 정답 txt 파일 두 개
  - 정답 파일의 경우 './answer' 폴더에 존재
- 출력 데이터 형식(선택): 결과 txt 파일
  - -o 옵션 없을 경우 상세 결과 없음
  - 파일 정리를 위해 되도록이면 './logs' 폴더 내에 생성할 것

```sh
./evaluate.py -i [예측 txt 파일] -a [정답 txt 파일] (-o [결과 txt 파일])
```

## 입력 형식

- 입력 형식 구성 위한 프로그램은 './temp' 폴더에 자유롭게 작성할 것
- 각 줄마다 결과 하나씩
  - '\n'으로 구분하여 입력받음

## 정답 리스트

#!/usr/bin/env python3
import argparse

if __name__ == "__main__":
    # ./evaluate.py -i [예측 txt 파일] -a [정답 txt 파일] (-o [결과 txt 파일])
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True)
    parser.add_argument('-a', '--answer', type=str, required=True)
    parser.add_argument('-o', '--output', type=str, default=None)
    args = parser.parse_args()

    # 예측 파일에서 한 줄씩 읽어서 리스트에 저장
    with open(args.input, 'r') as f:
        lines = f.readlines()
    pred = [line.strip() for line in lines]

    # 정답 파일에서 한 줄씩 읽어서 리스트에 저장
    with open(args.answer, 'r') as f:
        lines = f.readlines()
    ans = [line.strip() for line in lines]

    # 예측 결과와 정답을 비교하여 정확도 계산
    logs = ""
    correct = 0
    for i in range(len(pred)):
        if pred[i] == ans[i]:
            correct += 1
        else:
            logs += "Incorrect:\n"
            logs += "Predicted: {}\n".format(pred[i])
            logs += "Answer: {}\n".format(ans[i])
            logs += "----------------------------------------\n"
    accuracy = correct / len(pred)
    logs += "Total: {}\n".format(len(pred))
    logs += "Accuracy: {:.2f}%".format(accuracy * 100)
    print("Total: {}".format(len(pred)))
    print("Accuracy: {:.2f}%".format(accuracy * 100))
    if args.output is not None:
        with open(args.output, 'w') as f:
            f.write(logs)

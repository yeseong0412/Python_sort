import random

sorted_list = []  # 합병정렬시 사용


# 선택 정렬
def selection_sort(lst):
    # 리스트의 각 요소를 순회
    for i in range(len(lst)):
        # 가장 작은 요소의 인덱스를 찾는다
        min_idx = i
        for j in range(i + 1, len(lst)):
            # 현재 요소가 이전에 찾은 가장 작은 요소보다 작으면, 그 요소의 인덱스를 저장
            if lst[j] < lst[min_idx]:
                min_idx = j
        # 가장 작은 요소를 현재 요소와 교환
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    # 정렬된 리스트 반환
    return lst


# 삽입 정렬
def insertion_sort(lst):
    # 리스트의 첫 번째 요소부터 마지막 요소까지 순회
    for i in range(1, len(lst)):
        # 현재 요소를 key로 저장
        key = lst[i]
        # key의 이전 요소부터 시작하여, key보다 큰 요소를 오른쪽으로 이동
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        # key를 정렬된 위치에 삽입
        lst[j + 1] = key
    # 정렬된 리스트 반환
    return lst


# 버블 정렬
def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1, 0, -1):  # 리스트의 마지막 요소부터 첫 번째 요소까지 역순으로 순회
        for j in range(i):  # 첫 번째 요소부터 마지막에서 i번째 요소까지 순회
            if lst[j] > lst[j + 1]:  # 현재 요소가 다음 요소보다 크면 두 요소를 교환
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# 퀵 정렬
def quick_sort(A, left, right):
    # - A: List[int] - 정렬할 입력 배열
    # - left: int - 정렬할 범위의 왼쪽 인덱스
    # - right: int - 정렬할 범위의 오른쪽 인덱스

    if left < right:
        # 포인터 초기화
        i = left + 1
        j = right
        pivot = A[left]

        # 파티션 단계
        while i <= j:
            while i <= right and A[i] <= pivot:
                i += 1
            while j >= left and A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]

        # 피벗을 올바른 위치로 이동
        A[left], A[j] = A[j], A[left]

        # 두 파티션에 대한 재귀 호출
        quick_sort(A, left, j - 1)
        quick_sort(A, j + 1, right)


# 합병 정렬
def merge_sort(A, left, right):
    global sorted_list
    if left < right:
        mid = (left + right) // 2  # 분할
        merge_sort(A, left, mid)  # 분할
        merge_sort(A, mid + 1, right)  # 분할
        sorted_list = [0] * len(A)  # sorted_list를 0으로 초기화
        merge(A, left, mid, right)  # 합병


# 합병 정렬
def merge(A, left, mid, right):
    i = left  # 왼쪽 리스트의 첫 번째 인덱스
    j = mid + 1  # 오른쪽 리스트의 첫 번째 인덱스
    k = left  # 정렬될 리스트의 첫 번째 인덱스
    # 분할된 리스트의 합병
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_list[k] = A[i]
            i, k = i + 1, k + 1
        else:
            sorted_list[k] = A[j]
            j, k = j + 1, k + 1
    # 남아있는 리스트의 복사
    while i <= mid:
        sorted_list[k] = A[i]
        i, k = i + 1, k + 1
    while j <= right:
        sorted_list[k] = A[j]
        j, k = j + 1, k + 1
    # 임시(sorted_list) 리스트를 원래(A) 리스트로 복사
    A[left: right + 1] = sorted_list[left: right + 1]


# 힙 정렬 1
def heapify(lst, n, i):
    # 현재 노드를 가장 큰 값으로 설정
    largest = i
    # 왼쪽 자식 노드의 인덱스 계산
    l = 2 * i
    # 오른쪽 자식 노드의 인덱스 계산
    r = 2 * i + 1

    # 왼쪽 자식이 힙의 크기 내에 있고, 현재 값보다 크면 largest를 왼쪽 자식으로 업데이트
    if l <= n and lst[i - 1] < lst[l - 1]:
        largest = l
    # 오른쪽 자식이 힙의 크기 내에 있고, 현재 값보다 크면 largest를 오른쪽 자식으로 업데이트
    if r <= n and lst[largest - 1] < lst[r - 1]:
        largest = r

    # largest가 변경되었다면 현재 노드와 largest 노드의 값을 교환하고 다시 heapify 호출
    if largest != i:
        lst[i - 1], lst[largest - 1] = lst[largest - 1], lst[i - 1]
        heapify(lst, n, largest)

# 힙 정렬 1
def heapSort(lst):
    n = len(lst)
    # 최대 힙을 구성
    for i in range(n // 2, 0, -1):
        heapify(lst, n, i)
    # 힙에서 원소 하나씩 꺼내어 정렬
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 1)
    return lst

# 힙 정렬 2
def heapPush(heap, n):
    # 힙에 원소를 추가하고 힙 속성을 유지
    heap.append(n)
    i = len(heap) - 1
    while i != 0 and n > heap[i // 2]:
        heap[i] = heap[i // 2]
        i //= 2
    heap[i] = n

# 힙 정렬 2
def heapPop(heap):
    # 힙에서 최댓값을 제거하고 반환
    size = len(heap) - 1
    if size == 0:
        return None
    p = 0
    i = 1
    root = heap[0]
    last = heap[size]
    while i <= size:
        if i < size and heap[i] < heap[i + 1]:
            i += 1
        if last >= heap[i]:
            break
        heap[p] = heap[i]
        p = i
        i *= 2
    heap[p] = last
    heap.pop()
    return root

# 힙 정렬 2
def heap_sort(lst):
    # 리스트를 힙에 넣고 다시 꺼내어 정렬
    heap = [0]
    for e in lst:
        heapPush(heap, e)
    for i in range(1, len(lst) + 1):
        lst[-i] = heapPop(heap)
    return lst

# 메뉴
def print_menu():
    print("1. 선택 정렬")
    print("2. 삽입 정렬")
    print("3. 버블 정렬")
    print("4. 퀵 정렬")
    print("5. 합병 정렬")
    print("6. 힙 정렬")
    print("7. 종료")


# 메인 함수
def main():
    while True:
        # 리스트 생성
        lst = random.sample(range(101), 25)
        print_menu()
        choice = input("번호를 선택하세요: ")
        if choice == "1":
            print("<선택 정렬>")
            print("정렬 전: ", lst)
            print("정렬 후: ", selection_sort(lst))
        elif choice == "2":
            print("<삽입 정렬>")
            print("정렬 전: ", lst)
            print("정렬 후: ", insertion_sort(lst))
        elif choice == "3":
            print("<버블 정렬>")
            print("정렬 전: ", lst)
            print("정렬 후: ", bubble_sort(lst))
        elif choice == "4":
            print("<퀵 정렬>")
            print("정렬 전: ", lst)
            quick_sort(lst, 0, len(lst) - 1)
            print("정렬 후: ", lst)
        elif choice == "5":
            print("<합병 정렬>")
            print("정렬 전: ", lst)
            merge_sort(lst, 0, len(lst) - 1)
            print("정렬 후: ", lst)
        elif choice == "6":
            print("<힙 정렬>")
            lst1=list(lst)
            lst2=list(lst)
            print("힙 1번")
            print("정렬 전: ", lst1)
            print("정렬 후: ", heapSort(lst))
            print("힙 2번")
            print("정렬 전: ", lst2)
            print("정렬 후: ", heap_sort(lst2))
        elif choice == "7":
            exit("<종료>")
        else:
            print('<번호 오류>')


if __name__ == "__main__":
    main()

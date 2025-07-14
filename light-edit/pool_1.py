from multiprocessing import Pool


def streaming_reverse(texts, num_processes):
    rev_list = []
    with Pool(processes=num_processes) as pool:
        result_iterator = pool.imap(reversed, texts)
        for result in result_iterator:
            rev_list.append("".join(result))
    return rev_list


if __name__ == "__main__":
    texts = input().split()
    num_processes = int(input())

    result = (streaming_reverse(texts, num_processes))
    print(*result)

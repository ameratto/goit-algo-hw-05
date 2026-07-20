import sys
import re


def parse_log_line(line: str) -> dict[str, str]:
    if re.search(r'(\d+-\d+-\d+) (\d+:\d+:\d+) ([^\d\s]+) (\w*)', line):
    # 2024-01-22 08:30:01 INFO User logged in successfully.
        data, time, level, *text = line.split()
        return {"data": data, "time": time, "level": level, "text": ' '.join(list(text))}
    return {}

def load_logs(filepath: str) -> list[dict[str, str]]:
    try:
        logs = []
        with open(filepath, 'r', encoding="utf-8") as f:
            file_lines = [f.strip() for f in f.readlines()]
            for line in file_lines:
                logs.append(parse_log_line(line))
            return logs
    except FileNotFoundError:
        return []


def filter_logs_by_level(logs: list, level: str) -> list[dict[str,str]]:
    match level:
        case "info":
            return [line for line in logs if line["level"].lower() == "info"]
        case "debug":
            return [line for line in logs if line["level"].lower() == "debug"]
        case "error":
            return [line for line in logs if line["level"].lower() == "error"]
        case "warning":
            return [line for line in logs if line["level"].lower() == "warning"]
        case _: return []


def count_logs_by_level(logs: list) -> dict[str, int]:
    logs_level_list = {}
    for log in logs:
        try:
            if not log["level"] in logs_level_list:
                logs_level_list[str(log["level"])] = 1
            else:
                logs_level_list[str(log["level"])] += 1
        except KeyError:
            return {}
    return logs_level_list


def display_log_counts(counts: dict[str, int]) -> None:
    print(f"{'Рівень логування':<20} | {'Кількість'}")
    print("-" * 35)
    for level, count in counts.items():
        print(f"{str(level):<20} | {counts[str(level)]}")


def main():
    if sys.argv[1:]:
        path, *level = sys.argv[1:]
        logs = load_logs(path)
        display_log_counts(count_logs_by_level(logs))
        if level:
            logs = filter_logs_by_level(load_logs(str(path)), str(''.join(level)))
            for log in logs:
                print(f"{' '.join(log.values())}")


if __name__ == "__main__":
    main()

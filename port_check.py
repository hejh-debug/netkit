HIGH_RISK = {21,23,445,1433,3306,3389,6379}
ok_count = 0
high_count = 0
bad_count = 0
while True:
  text = input("请输入端口(q 结束):").strip()
  if text.lower() == "q":
    break
  if not text:
    print("端口不能为空")
    continue
  if not text.isdigit():
    bad_count += 1
    print(f"[无效] {text} 不是数字端口")
    continue
  port = int(text)
  if port < 1 or port > 65535:
    bad_count += 1
    print(f"[无效] {port} 超出端口范围")
    continue
  ok_count += 1
  if port in HIGH_RISK:
    high_count += 1
    print(f"[高危] {port} 需额外审批")
  else:
    print(f"[普通] {port}")

print(f"合法 {ok_count} 个，其中高危 {high_count} 个，无效{bad_count} 个")

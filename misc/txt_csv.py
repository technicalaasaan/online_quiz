import csv
import re
import pickle
import shelve

# f = open(r"C:\Users\mzmmo\OneDrive\Desktop\sathyabama_pdf\july_batch\sample.pkl", 'rb')
# print(f.read())
# f = shelve.open(r"C:\Users\mzmmo\OneDrive\Desktop\sathyabama_pdf\july_batch\hello.dbm")
# print(dict(f))

# f['country'] = 'india'

# f.close()
# print(pickle.load(f))
# print(pickle.load(f))
# print(pickle.load(f))
# print(pickle.load(f))
# exit()

class Converter:
	def read_txt(self, path):
		f = open(path)
		datas = f.read().split('|')
		out = []
		for que in datas:
			# print(que)
			# if que.startswith("18)"):
			# 	print('yes')
			# else:
			# 	continue
			each_ques = {
					# "question": re.split("\d\).*a\)", que)[0].replace(r"1) ", "").split("\na)")[0].strip(),
					"question": que.split("\na)")[0].strip(),
					"option1": que.split("a)")[1].split("b)")[0].strip(),
					"option2": que.split("b)")[1].split("c)")[0].strip(),
					"option3": que.split("c)")[1].split("d)")[0].strip(),
					"option4": que.split("d)")[1].split("ans:")[0].strip(),
					"answer": que.split("ans:")[1].strip()
			}
			out.append(each_ques)
		return out

	def write(self):
		resp = self.read_txt(r"C:\Users\mzmmo\OneDrive\Desktop\sathyabama_pdf\python_ques_ans.txt")
		with open("ques.csv", "w") as f:
			writer = csv.writer(f)
			writer.writerow(resp[0].keys())
			for row in resp:
				if not row:
					continue
				writer.writerow(row.values())
		return "success"

	def sql_cmd(self):
		resp = self.read_txt(r"C:\Users\mzmmo\OneDrive\Desktop\sathyabama_pdf\python_ques_ans.txt")
		for row in resp:
			header = str(tuple(row.keys())).replace("'", "")
			query = f"insert into quiz {header} values {tuple(row.values())};"
			print(query)


cls = Converter()
cls.sql_cmd()
# cls.read_txt(r"C:\Users\mzmmo\OneDrive\Desktop\sathyabama_pdf\python_ques_ans.txt")
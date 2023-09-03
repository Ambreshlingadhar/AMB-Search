import pickle

openai_key = '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'

save_data = {"openai_key": openai_key}

pickle.dump(save_data,open('awesome.pkl','wb'))
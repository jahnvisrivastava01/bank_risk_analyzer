import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("bank_data.csv")

print("Bank Data")
print(df)

total_balance=df["Balance"].sum()
print("\nTotal Bank Balance:",total_balance)

avg_balance=df["Balance"].mean()
print("Average Balance:",avg_balance)

top_customer=df.loc[df["Balance"].idxmax()]

print("\nTop Customer:")
print(top_customer["Name"],"with balance=",top_customer["Balance"])

def get_risk(row):
    if row["Balance"] < 10000 and row["Transactions"] >30:
        return "High Risk"
    elif row["Withdrawals"] and row["Deposits"] * 2:
        return "Fraud Alert"
    else:
        return "Safe"
    
df["Risk Level"] = df.apply(get_risk,axis=1)

print("\nRisk Analysis")
print(df[["Name","Risk Level"]])

plt.figure()
plt.bar(df["Name"],df["Transactions"])
plt.title("Transactions per customer")
plt.xlabel("Customer")
plt.ylabel("Transactions")

plt.show()

risk_counts=df["Risk Level"].value_counts()

plt.figure()
plt.pie(risk_counts,labels=risk_counts.index,autopct='%1.1f')
plt.title("Risk Distribution")

plt.show()

top3 = df.sort_values(by="Balance", ascending=False).head(3)

print("\nTop 3 Customers:")
print(top3[["Name", "Balance"]])

print("\nRisk Summary:")
print(df["Risk Level"].value_counts())

df.to_csv("analysis_output.csv",index=False)
print("\nResults saved to analysis_output.csv")
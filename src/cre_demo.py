import os
import pandas as pd

data = r"D:\Python313\Bảo mật ứng dụng hệ thống\BTL_Bao_mat_ung_dung_he_thong\data\raw\cicids2017_500k.csv"
data_output = r"D:\Python313\Bảo mật ứng dụng hệ thống\BTL_Bao_mat_ung_dung_he_thong\data\output"

os.makedirs(data_output, exist_ok=True)

benign_sp = []
attack_sp = []


df = pd.read_csv(data)
df.columns = df.columns.str.strip()

benign = df[df["Label"] == "BENIGN"]
attack = df[df["Label"] != "BENIGN"]

benign_df = benign.sample(
    n=min(600, len(benign)),
    random_state=42
)

attack_df = attack.sample(
    n=min(600, len(attack)),
    random_state=42
)

demo_benign = benign_df.sample(n=300, random_state=42)
demo_attack = attack_df.sample(n=300, random_state=42)

demo_mixed = pd.concat([
    benign_df.sample(n=250, random_state=42),
    attack_df.sample(n=50, random_state=42)
]).sample(frac=1, random_state=42)

demo_high_risk = pd.concat([
    benign_df.sample(n=100, random_state=42),
    attack_df.sample(n=200, random_state=42)
]).sample(frac=1, random_state=42)

demo_benign.to_csv(f"{data_output}/demo_benign.csv", index=False, encoding="utf-8-sig")
demo_attack.to_csv(f"{data_output}/demo_attack.csv", index=False, encoding="utf-8-sig")
demo_mixed.to_csv(f"{data_output}/demo_mixed.csv", index=False, encoding="utf-8-sig")
demo_high_risk.to_csv(f"{data_output}/demo_high_risk.csv", index=False, encoding="utf-8-sig")

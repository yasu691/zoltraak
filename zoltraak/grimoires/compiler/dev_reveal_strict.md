# 要件定義書
# Reveal.jsを用いたプレゼンテーション資料作成の要件定義

## 目的
- Reveal.jsを使用して{prompt}をお題としたプレゼンテーション資料を作成する

## ページ
以下を参考にお題に応じて改変

```
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│    Presenter  │ │    Revealer   │ │     Slide     │
├───────────────┤ ├───────────────┤ ├───────────────┤
│ goto(index)   │ │ goto(index)   │ │ render()      │
│               │ │               │ │               │
│ getSlide()    │ │               │ │               │
│               │ │               │ │               │
│               │ │               │ │               │
└───────────────┘ └───────────────┘ └───────────────┘
```

## 機能要件
- 以下index.htmlと使い方のリードミーのみ出力
- JavaScriptの資産を最大限活用し、おしゃれなプレゼンテーションを作成する

index.html
HTML5 で書かれていることを宣言
ページの言語が日本語であることを指定
ページのメタデータを含むヘッダー部分の開始
文字エンコーディングを UTF-8 に設定
レスポンシブデザイン用のビューポート設定
デバイス幅に合わせて表示
初期倍率は1.0 
ユーザーによる拡大縮小は禁止
ページのタイトルを設定
reveal.js のリセット CSS を読み込み
reveal.js の本体 CSS を読み込み
reveal.js のテーマ CSS (white) を読み込み
Google Fonts から Noto Sans JP を読み込み
ページ固有のスタイルを定義
reveal クラスのスタイル
 フォントを Noto Sans JP に設定
 フォントサイズを 42px に設定
 フォントウェイトを normal に設定
reveal クラス内の h1~h4 のスタイル
 テキストの変形を無効化
reveal クラス内の section 内の img のスタイル
 画像のボーダーを無効化
 画像のボックスシャドウを無効化
た内容を真面目かつ徹底的に議論する 
ページの本文部分の開始
reveal.js のルート要素
スライドのコンテナ要素
背景画像付きのセクション (スライド)
背景画像の URL を指定 (Unsplash からランダムな靴下の画像を取得)
背景画像の不透明度を 0.5 に設定
スライドのタイトル
新しいセクション (スライド)
スライドのサブタイトル
箇条書きのリスト 
 リストアイテム (フラグメント付き)
 リストアイテム (フラグメント付き)
 リストアイテム (フラグメント付き)
新しいセクション (スライド)
スライド遷移効果を convex に設定
スライドのサブタイトル
段落
画像 (Unsplash からランダムな泥棒の画像を取得)
新しいセクション (スライド)
スライド遷移効果を convex に設定
スライドのサブタイトル
段落
画像 (Unsplash からランダムなワームホールの画像を取得)
新しいセクション (スライド)
スライド遷移効果を zoom に設定
スライドのサブタイトル
段落
画像 (Unsplash からランダムな靴下の画像を取得)
新しいセクション (スライド)
スライド遷移効果を zoom に設定
スライドのサブタイトル
段落
画像 (Unsplash からランダムな洗濯機の画像を取得)
新しいセクション (スライド)
スライド遷移効果を fade に設定
スライドのサブタイトル
段落
画像 (Unsplash からランダムな量子もつれの画像を取得)
新しいセクション (スライド)
スライド遷移効果を fade に設定
スライドのサブタイトル
段落
画像 (Unsplash からランダムな離婚の画像を取得)
新しいセクション (スライド)
スライド遷移効果を slide に設定
スライドのサブタイトル
段落
段落 (フラグメント付き)
背景画像付きのセクション (スライド)
背景画像の URL を指定 (Unsplash からランダムなミステリーの画像を取得)
背景画像の不透明度を 0.8 に設定
スライドのタイトル
段落
reveal.js の本体スクリプトを読み込み
reveal.js のズームプラグインを読み込み
ページ固有のスクリプトを定義
reveal.js を初期化
 コントロール (ナビゲーション) を有効化
 進捗バーを有効化
 スライドを中央揃えにする
 URL ハッシュを有効化
 使用するプラグインを指定 (ズームプラグイン)
スライド枚数は10枚とする
コードは一切省略せずに記載する
アニメーションを取り入れ、リッチな見た目にする
画像はunsplashから取得する
色は白を基調としたカラフルな色使いにする
様々なレイアウトを使用し、アニメーションを活用する
おしゃれな日本語フォントを使用する

## 非機能要件
- アセットはCDNから取得する
- パフォーマンスに配慮し、高速に動作するようにする
- モバイルデバイスでも快適に閲覧できるようにレスポンシブデザインを適用する

## 制約事項 
- Reveal.jsを使用すること
- {prompt}というお題に沿った内容であること
- 指定された要件を満たすこと
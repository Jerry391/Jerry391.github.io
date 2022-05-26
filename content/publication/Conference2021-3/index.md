---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Visualization Transfer from 2D Image to 3D Volume"
authors:
  - Dan Yang
  - Zhiwei Mao
  - admin
  - Siru Chen
  - Xiaodong Wen
  - Meng Jiang
  - Yiping Wu
date: 2021-04-26T10:52:53+08:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2022-05-26T10:52:53+08:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["9"]

# Publication name and optional abbreviated publication name.
publication: "*In *Proceedings of the 14th IEEE Pacific Visualization Symposium*"
publication_short: "In *PacificVis 2021*"

abstract: "Traditional visualization work focuses on collaborative visualization and 2-D data analysis, which is limited when analyzing complex 3-D data. In 3-D volume data analysis, visualization transforms the invisible phenomena in volume data into visible, revealing the rich connotations contained in volume data. It enhances domain experts’ awareness of three-dimensional space. However, it is complicated for experts to mark target objects in 3-D images, because it is very difficult to select the target point in the 3-D image accurately. If all seed points can be automatically recommended to the 2-D image, and after manual selection, the required structure can be marked in the 3-D image by the seed point tracking algorithm, then domain experts will be able to greatly improve the efficiency of data interpretation. In this paper, we propose an interactive visualization system based on client server seed point recommendation and tracking, which consists of a 3-D volume explorer and a 2-D slice analyzer, to help domain experts fully utilize their background domain knowledge to illustrate different parts of the data. The system realizes multi-user interaction and can run on multi terminal devices because the client-side calculation is very small. It allows taking full advantage of the hardware resources because all the computation intensive tasks especially for the whole data rendering can be allocated to the powerful server while the light-weight tasks can be allocated to the portable clients. For example, the brain surgeon expert, pulmonologist, and cardiologist can visualize and analyze the different subsets of the volumetric scientific data, that is, the corresponding subvolumes of the brain, heart, lungs, and blood vessels. We calculate the image entropy of all slices on the server side, and select the slice with the largest entropy, and then recommend all seed points according to the seed point recommendation algorithm based on meanshift. In addition, we also design a seed point tracking algorithm based on continuous scale space theory, which realizes the migration from 2-D to 3-D."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
links:
- name: Link
  url: http://vis.tju.edu.cn/pvis2021/program_posters.html
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

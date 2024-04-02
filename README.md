<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EYIJ Team</title>
<link rel="stylesheet" href="https://s3.ap-northeast-2.amazonaws.com/materials.spartacodingclub.kr/easygpt/default.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
        crossorigin="anonymous"></script>
<style>
        body {
                background-color: #ffffff; /* 전체 페이지 배경색을 흰색으로 설정 */
                color: #000000; /* 기본 글씨색을 검정으로 설정 */
                }

                .hero {
                background-color: #0b2c4c; /* 어두운 배경색 설정 */
                color: #ffffff; /* 흰색 글씨색 설정 */
                padding: 20px 0; /* 패딩 추가 */
                text-align: center; /* 텍스트 가운데 정렬 */
                }

                .navbar {
                    background-color: #ffffff; /* Navbar 배경색을 흰색으로 설정 */
                }

                .row {
                display: flex; /* Display flex to make cards horizontal */
                flex-wrap: wrap; /* Allow wrapping of cards */
                gap: 20px; /* Space between cards */
                }
                .card {
                flex: 1; /* Each card takes up equal space */
                height: 100%; /* 부모 요소의 높이에 맞춤 */
                border: none; /* 카드 테두리 제거 */
                background-color: #f8f9fa; /* 옅은 회색 배경 */
                transition: transform 0.3s ease; /* 부드러운 애니메이션 추가 */
                }
                .card-img-top {
                max-height: 230px; /* 이미지 최대 높이 설정 */
                object-fit: cover; /* 이미지 비율을 유지하면서 영역 채움 */
                width: auto; /* 너비 자동 조절 */
                height: auto; /* 높이 자동 조절 */
                max-width: 100%; /* 최대 너비를 카드 너비에 맞춤 */
                }
                /* 추가한 스타일 */
                .container-mt-5 {
                margin-top: 30px; /* 원하는 여백 크기로 조절 */
                }

                .card:hover {
                transform: scale(1.09); /* 마우스를 올릴 때 카드가 약간 커지도록 설정 */
                }
</style>
</head>

<body>
<nav class="navbar border-bottom border-bottom-dark d-flex justify-content-end" data-bs-theme="dark">
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{{ url_for('home') }}">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{{ url_for('Team Intro') }}">Team Intro</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">게시판</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">로그인/회원가입</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</nav>

<div class="hero">
  <h1 class="text-white">EYIJ Team Introduction</h1>
  <h2 class="text-white">AI 6기 14조
  <h3 class="text-white">친해지는데 시간이 걸리는 스타일이에요</h3>
    </div>

    <div class="container mt-5">
      <img
        src="https://kksoo0131.github.io/assets/img/thumbnail-image.png"
        class="img-fluid"
        alt="New Team Member"
        style="width: 100%" />
    </div>

    <!-- Rest of the Cards -->
<!-- 현현섭 -->
<div class="col-md-4 mb-4"> <!-- 여기에 현현섭 추가 -->
  <div class="card" style="width: 18rem;">
  <img src="https://e1.pxfuel.com/desktop-wallpaper/321/342/desktop-wallpaper-crayon-shin-chan-doraemon-and-shinchan.jpg" class="card-img-top" alt="현현섭">
  <div class="card-body">
  <h5 class="card-title">현현섭</h5>
  <h6 class="card-subtitle mb-2 text-muted">
  <span style="color: black;font-weight: bold;">INTP</span>
  </h6>
  <p class="card-text">
    현현섭현현섭현현섭
  </p>
  <a
                      href="https://www.bang-olufsen.com/ko/kr/speakers/beosound-a1"
  class="btn btn-primary"
          target="_blank"
          rel="noopener noreferrer"
          >
          github 주소 보기
  </a>
  </div>
  </div>
  </div>
  
  
  
  <!--이훈희 -->
  <div class="col-md-4">
  <div class="card" style="width: 18rem;">
  <img src="https://origami-database.com/wp-content/uploads/DSC03328-export-3000x3000.jpg" class="card-img-top" alt="이훈희">
  <div class="card-body">
  <h5 class="card-title">이훈희</h5>
  <h6 class="card-subtitle mb-2 text-muted">
  <span style="color: black;font-weight: bold;">INTP</span>
  </h6>
  <p class="card-text">
    이훈희
  </p>
  <a
                      href="https://github.com/hunhee92/hunhee92"
  class="btn btn-primary"
          target="_blank"
          rel="noopener noreferrer"
          >
          github 주소 보기
  </a>
  </div>
  </div>
  </div>
  
  <!--이경은 -->
  <div class="col-md-4">
    <div class="card" style="width: 18rem;">
    <img src="https://origami-database.com/wp-content/uploads/DSC03328-export-3000x3000.jpg" class="card-img-top" alt="이훈희">
    <div class="card-body">
    <h5 class="card-title">이경은</h5>
    <h6 class="card-subtitle mb-2 text-muted">
    <span style="color: black;font-weight: bold;">INTP</span>
    </h6>
    <p class="card-text">
      이경은
    </p>
    <a
                        href="https://github.com/Yuancod"
    class="btn btn-primary"
            target="_blank"
            rel="noopener noreferrer"
            >
            github 주소 보기
    </a>
    </div>
    </div>
    </div>
  
  <!-- 황원욱 -->
  <div class="col-md-4">
  <div class="card" style="width: 18rem;">
  <img src="https://origami-database.com/wp-content/uploads/DSC03329-export.jpg" class="card-img-top" alt="황원욱">
  <div class="card-body">
  <h5 class="card-title">황원욱</h5>
  <h6 class="card-subtitle mb-2 text-muted">
  <span style="color: black;font-weight: bold;">ENTP</span>
  </h6>
  <p class="card-text">
    황원욱황원욱
  </p>
  <a
                      href="https://github.com/hwangwonwook/hwangwonwook"
  class="btn btn-primary"
          target="_blank"
          rel="noopener noreferrer"
          >
          github 주소 보기
  </a>
  </div>
  </div>
  </div>
  
  
  <!-- 오규선 -->
  <div class="col-md-4">
  <div class="card" style="width: 18rem">
  <img
                src="https://origami-database.com/wp-content/uploads/DSC01032-export-3000x3000.jpg"
  class="card-img-top"
          alt="오규선"
          />
  <div class="card-body">
  <h5 class="card-title">오규선</h5>
  <h6 class="card-subtitle mb-2 text-muted">
  <span style="color: black;font-weight: bold;">ENTJ</span>
  </h6>
  <p class="card-text">
    오규선오규선오규선
  </p>
  <a
                  href="https://github.com/AUD-OH"
  class="btn btn-primary"
          target="_blank"
          rel="noopener noreferrer"
          >
          github 주소 보기
  </a>
  </div>
  </div>
  </div>
  </div>
  </div>
  </body>
  </html>
  <div class="container mt-5">
  <div class="row">
  

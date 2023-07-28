import 'package:flutter/material.dart';

class HomeView extends StatelessWidget {
  const HomeView({super.key});
  final gradient = const LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [Colors.white, Color.fromRGBO(239, 59, 54, 1)],
    stops: [0.2, 0.9],
  );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const SizedBox(
                height: 30,
              ),
              ShaderMask(
                shaderCallback: (Rect bounds) {
                  return gradient.createShader(bounds);
                },
                child: const Center(
                  child: Text(
                    'Genimate',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 40.0,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ),
              ),
              const SizedBox(
                height: 5,
              ),
              const Text(
                "시켜줘. FLYAI 명예 기상캐스터!",
                style: TextStyle(
                    color: Color.fromRGBO(239, 59, 54, 1),
                    fontSize: 15,
                    fontWeight: FontWeight.w500),
              ),
              const SizedBox(
                height: 3,
              ),
              const Text(
                "보라매의 날씨를 메일로 알려주는 서비스입니다.",
                style: TextStyle(
                    color: Colors.black87,
                    fontSize: 12,
                    fontWeight: FontWeight.w500),
              ),
              const SizedBox(
                height: 15,
              ),
              Center(
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(20.0), // 테두리 둥글기 조절
                  child: Image.asset('assets/home_adot.gif'), // GIF 이미지 경로 설정
                ),
              ),
              const SizedBox(
                height: 15,
              ),
              ElevatedButton(
                onPressed: () {
                  // 버튼을 클릭하면 이메일 작성 페이지로 이동
                  Navigator.pushNamed(context, '/compose_email');
                },
                style: ElevatedButton.styleFrom(
                    backgroundColor: const Color.fromRGBO(239, 59, 54, 1),
                    padding: const EdgeInsets.symmetric(
                        horizontal: 15, vertical: 15), // 패딩 설정
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(7), // 모서리 둥글기 설정
                    ),
                    shadowColor: Colors.black12),
                child: const Text(
                  '구독하기',
                  style: TextStyle(fontSize: 15, fontWeight: FontWeight.w300),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

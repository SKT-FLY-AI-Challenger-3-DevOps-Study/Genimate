import 'package:flutter/material.dart';
import 'package:genimate/views/breakpoint.dart';
import 'package:genimate/views/text_main.dart';

class HomeView extends StatelessWidget {
  const HomeView({super.key});

  @override
  Widget build(BuildContext context) {
    final double currenWidth = MediaQuery.of(context).size.width;
    var isWeb = currenWidth > BreakPoint.mobile ? true : false;

    return Scaffold(
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const MainText(),
              SizedBox(
                height: 400,
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
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w300,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

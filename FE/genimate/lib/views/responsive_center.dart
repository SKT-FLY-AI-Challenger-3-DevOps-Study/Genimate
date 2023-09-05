import 'package:flutter/material.dart';
import 'package:genimate/views/breakpoint.dart';

class ResponsiveCenter extends StatelessWidget {
  const ResponsiveCenter(
      {super.key,
      this.maxContentWidth = BreakPoint.mobile,
      this.padding = EdgeInsets.zero,
      required this.child});
  final double maxContentWidth;
  final EdgeInsetsGeometry padding;
  final Widget child;
  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: maxContentWidth,
      child: Padding(
        padding: padding,
        child: child,
      ),
    );
  }
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qhighdpiscaling_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 3.
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_HIGHDPISCALING)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qhighdpiscaling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/QList>
#include <QtCore/QStringView>
#include <QtGui/6.12.0/QtGui/qpa/qplatformscreen.h>

//  void QHighDpiScaling::initHighDpiScaling()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHighDpiScaling18initHighDpiScalingEv() {
  QHighDpiScaling::initHighDpiScaling();
}

//  void QHighDpiScaling::updateHighDpiScaling()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHighDpiScaling20updateHighDpiScalingEv() {
  QHighDpiScaling::updateHighDpiScaling();
}

//  void QHighDpiScaling::setGlobalFactor(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHighDpiScaling15setGlobalFactorEd(qreal factor) {
  QHighDpiScaling::setGlobalFactor(factor);
}

//  void QHighDpiScaling::setScreenFactor(QScreen *screen, qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHighDpiScaling15setScreenFactorEP7QScreend(
    QScreen *screen,
    qreal factor) {
  QHighDpiScaling::setScreenFactor(screen, factor);
}

//  bool QHighDpiScaling::isActive()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHighDpiScaling8isActiveEv() {
  return QHighDpiScaling::isActive();
}

//  ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const QPlatformScreen
//      *platformScreen, Point position)
extern "C" Q_DECL_EXPORT
QHighDpiScaling::ScaleAndOrigin *ritual_ZN15QHighDpiScaling14scaleAndOriginEPK15QPlatformScreenNS_5PointE(
    const QPlatformScreen *platformScreen,
    const QHighDpiScaling::Point *position) {
  return new QHighDpiScaling::ScaleAndOrigin(
      QHighDpiScaling::scaleAndOrigin(
          platformScreen,
          *position));
}

//  ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const QScreen *screen,
//      Point position)
extern "C" Q_DECL_EXPORT
QHighDpiScaling::ScaleAndOrigin *ritual_ZN15QHighDpiScaling14scaleAndOriginEPK7QScreenNS_5PointE(
    const QScreen *screen,
    const QHighDpiScaling::Point *position) {
  return new QHighDpiScaling::ScaleAndOrigin(
      QHighDpiScaling::scaleAndOrigin(
          screen,
          *position));
}

//  ScaleAndOrigin QHighDpiScaling::scaleAndOrigin(const QWindow
//      *platformScreen, Point position)
extern "C" Q_DECL_EXPORT
QHighDpiScaling::ScaleAndOrigin *ritual_ZN15QHighDpiScaling14scaleAndOriginEPK7QWindowNS_5PointE(
    const QWindow *platformScreen,
    const QHighDpiScaling::Point *position) {
  return new QHighDpiScaling::ScaleAndOrigin(
      QHighDpiScaling::scaleAndOrigin(
          platformScreen,
          *position));
}

//  QPoint QHighDpiScaling::mapPositionFromNative(const QPoint &pos, const
//      QPlatformScreen *platformScreen)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN15QHighDpiScaling21mapPositionFromNativeERK6QPointPK15QPlatformScreen(
    const QPoint *pos,
    const QPlatformScreen *platformScreen) {
  return new QPoint(
      QHighDpiScaling::mapPositionFromNative(
          *pos,
          platformScreen));
}

//  QPoint QHighDpiScaling::mapPositionToNative(const QPoint &pos, const
//      QPlatformScreen *platformScreen)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN15QHighDpiScaling19mapPositionToNativeERK6QPointPK15QPlatformScreen(
    const QPoint *pos,
    const QPlatformScreen *platformScreen) {
  return new QPoint(
      QHighDpiScaling::mapPositionToNative(
          *pos,
          platformScreen));
}

//  QDpi QHighDpiScaling::logicalDpi(const QScreen *screen)
extern "C" Q_DECL_EXPORT
QDpi *ritual_ZN15QHighDpiScaling10logicalDpiEPK7QScreen(
    const QScreen *screen) {
  return new QDpi(QHighDpiScaling::logicalDpi(screen));
}

//  qreal QHighDpiScaling::roundScaleFactor(qreal rawFactor)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN15QHighDpiScaling16roundScaleFactorEd(qreal rawFactor) {
  return QHighDpiScaling::roundScaleFactor(rawFactor);
}

//  qreal QHighDpiScaling::rawScaleFactor(const QPlatformScreen *screen)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN15QHighDpiScaling14rawScaleFactorEPK15QPlatformScreen(
    const QPlatformScreen *screen) {
  return QHighDpiScaling::rawScaleFactor(screen);
}

//  QDpi QHighDpiScaling::effectiveLogicalDpi(const QPlatformScreen *screen,
//      qreal rawFactor, qreal roundedFactor)
extern "C" Q_DECL_EXPORT
QDpi *ritual_ZN15QHighDpiScaling19effectiveLogicalDpiEPK15QPlatformScreendd(
    const QPlatformScreen *screen,
    qreal rawFactor,
    qreal roundedFactor) {
  return new QDpi(
      QHighDpiScaling::effectiveLogicalDpi(
          screen,
          rawFactor,
          roundedFactor));
}

//  qreal QHighDpiScaling::screenSubfactor(const QPlatformScreen *screen)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN15QHighDpiScaling15screenSubfactorEPK15QPlatformScreen(
    const QPlatformScreen *screen) {
  return QHighDpiScaling::screenSubfactor(screen);
}

//  QScreen *QHighDpiScaling::screenForPosition(Point position, QScreen
//      *guess)
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZN15QHighDpiScaling17screenForPositionENS_5PointEP7QScreen(
    const QHighDpiScaling::Point *position,
    QScreen *guess) {
  return QHighDpiScaling::screenForPosition(*position, guess);
}

//  QList<QHighDpiScaling::ScreenFactor>
//      QHighDpiScaling::parseScreenScaleFactorsSpec(QStringView
//      screenScaleFactors)
extern "C" Q_DECL_EXPORT
QList<QHighDpiScaling::ScreenFactor> *ritual_ZN15QHighDpiScaling27parseScreenScaleFactorsSpecE11QStringView(
    const QString *screenScaleFactors) {
  return new QList<QHighDpiScaling::ScreenFactor>(
      QHighDpiScaling::parseScreenScaleFactorsSpec(
          QStringView(*screenScaleFactors)));
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const ScreenFactor &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRKN15QHighDpiScaling12ScreenFactorE(
    const QDebug *a0,
    const QHighDpiScaling::ScreenFactor *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  a QDpi a ritual of QHighDpiScaling gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHighDpiScaling__QDpi(QDpi *self) {
  delete self;
}

//  a QList<QHighDpiScaling::ScreenFactor> a ritual of QHighDpiScaling gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHighDpiScaling__QList_QHighDpiScaling_ScreenFactor(
    QList<QHighDpiScaling::ScreenFactor> *self) {
  delete self;
}

//  static qreal QHighDpiScaling::factor<QScreen>(QScreen *context)
extern "C" Q_DECL_EXPORT
double ritual_ZN15QHighDpiScaling6factorI7QScreenEEdPT_(
    QScreen *context) {
  return QHighDpiScaling::factor<QScreen>(context);
}

//  static qreal QHighDpiScaling::factor<QWindow>(QWindow *context)
extern "C" Q_DECL_EXPORT
double ritual_ZN15QHighDpiScaling6factorI7QWindowEEdPT_(
    QWindow *context) {
  return QHighDpiScaling::factor<QWindow>(context);
}

//  static qreal QHighDpiScaling::factor<QPlatformScreen>(
//      QPlatformScreen *context)
extern "C" Q_DECL_EXPORT
double ritual_ZN15QHighDpiScaling6factorI15QPlatformScreenEEdPT_(
    QPlatformScreen *context) {
  return QHighDpiScaling::factor<QPlatformScreen>(context);
}

#endif  // !defined(QT_NO_HIGHDPISCALING)

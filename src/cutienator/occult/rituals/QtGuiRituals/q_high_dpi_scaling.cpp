//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qhighdpiscaling_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_HIGHDPISCALING)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qhighdpiscaling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

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

#endif  // !defined(QT_NO_HIGHDPISCALING)

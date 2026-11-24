//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/priv
//  ate/qquickfluentwinui3focusframe_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQuickControls2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3styleimplglobal_p.h>
#include <QtQuickControls2FluentWinUI3StyleImpl/QtQuickControls2FluentWinUI3StyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3focusframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickFluentWinUI3FocusFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickFluentWinUI3FocusFrame10metaObjectEv(
    const QQuickFluentWinUI3FocusFrame *self) {
  return self->metaObject();
}

//  QString QQuickFluentWinUI3FocusFrame::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuickFluentWinUI3FocusFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFluentWinUI3FocusFrame::tr(s, c, n));
}

//  QQuickFluentWinUI3FocusFrame::QQuickFluentWinUI3FocusFrame()
extern "C" Q_DECL_EXPORT
QQuickFluentWinUI3FocusFrame *ritual_ZN28QQuickFluentWinUI3FocusFrameC1Ev() {
  return new QQuickFluentWinUI3FocusFrame();
}

//  QQuickItem *QQuickFluentWinUI3FocusFrame::createFocusFrame(QQmlContext
//      *context)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN28QQuickFluentWinUI3FocusFrame16createFocusFrameEP11QQmlContext(
    QQuickFluentWinUI3FocusFrame *self,
    QQmlContext *context) {
  return self->createFocusFrame(context);
}

//  void QQuickFluentWinUI3FocusFrame::moveToItem(QQuickControl *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickFluentWinUI3FocusFrame10moveToItemEP13QQuickControl(
    QQuickFluentWinUI3FocusFrame *self,
    QQuickControl *item) {
  self->moveToItem(item);
}

//  QQuickControl *QQuickFluentWinUI3FocusFrame::getFocusTarget(QQuickControl
//      *focusItem) const
extern "C" Q_DECL_EXPORT
QQuickControl *ritual_ZNK28QQuickFluentWinUI3FocusFrame14getFocusTargetEP13QQuickControl(
    const QQuickFluentWinUI3FocusFrame *self,
    QQuickControl *focusItem) {
  return self->getFocusTarget(focusItem);
}

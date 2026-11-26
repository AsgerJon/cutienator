//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickpopupwindow_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupwindow_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <optional>
#include <QtCore/QPoint>

//  Only a class built on QQuickPopupWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPopupWindow : QQuickPopupWindow {
  using QQuickPopupWindow::hideEvent;
  using QQuickPopupWindow::moveEvent;
  using QQuickPopupWindow::resizeEvent;
  using QQuickPopupWindow::event;
};

//  const QMetaObject *QQuickPopupWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickPopupWindow10metaObjectEv(
    const QQuickPopupWindow *self) {
  return self->metaObject();
}

//  void *QQuickPopupWindow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickPopupWindow11qt_metacastEPKc(
    QQuickPopupWindow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPopupWindow::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickPopupWindow11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPopupWindow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPopupWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickPopupWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPopupWindow::tr(s, c, n));
}

//  void QQuickPopupWindow::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow22qt_qmlMarker_anonymousEv(
    QQuickPopupWindow *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickPopupWindow::QQuickPopupWindow(QQuickPopup *popup, QWindow *parent)
extern "C" Q_DECL_EXPORT
QQuickPopupWindow *ritual_ZN17QQuickPopupWindowC1EP11QQuickPopupP7QWindow(
    QQuickPopup *popup,
    QWindow *parent) {
  return new QQuickPopupWindow(popup, parent);
}

//  QQuickPopup *QQuickPopupWindow::popup() const
extern "C" Q_DECL_EXPORT
QQuickPopup *ritual_ZNK17QQuickPopupWindow5popupEv(
    const QQuickPopupWindow *self) {
  return self->popup();
}

//  void QQuickPopupWindow::hideEvent(QHideEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow9hideEventEP10QHideEvent(
    QQuickPopupWindow *self,
    QHideEvent *e) {
  self->hideEvent(e);
}

//  void QQuickPopupWindow::moveEvent(QMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow9moveEventEP10QMoveEvent(
    QQuickPopupWindow *self,
    QMoveEvent *e) {
  self->moveEvent(e);
}

//  void QQuickPopupWindow::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow11resizeEventEP12QResizeEvent(
    QQuickPopupWindow *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

//  bool QQuickPopupWindow::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickPopupWindow5eventEP6QEvent(
    QQuickPopupWindow *self,
    QEvent *e) {
  return self->event(e);
}

//  void QQuickPopupWindow::windowChanged(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow13windowChangedEP7QWindow(
    QQuickPopupWindow *self,
    QWindow *window) {
  self->windowChanged(window);
}

//  std::optional<QPoint> QQuickPopupWindow::global2Local(const QPoint &pos)
//      const
extern "C" Q_DECL_EXPORT
std::optional<QPoint> *ritual_ZNK17QQuickPopupWindow12global2LocalERK6QPoint(
    const QQuickPopupWindow *self,
    const QPoint *pos) {
  return new std::optional<QPoint>(self->global2Local(*pos));
}

//  void QQuickPopupWindow::parentWindowXChanged(int newX)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow20parentWindowXChangedEi(
    QQuickPopupWindow *self,
    int newX) {
  self->parentWindowXChanged(newX);
}

//  void QQuickPopupWindow::parentWindowYChanged(int newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow20parentWindowYChangedEi(
    QQuickPopupWindow *self,
    int newY) {
  self->parentWindowYChanged(newY);
}

//  void QQuickPopupWindow::handlePopupPositionChangeFromWindowSystem(const
//      QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow41handlePopupPositionChangeFromWindowSystemERK6QPoint(
    QQuickPopupWindow *self,
    const QPoint *pos) {
  self->handlePopupPositionChangeFromWindowSystem(*pos);
}

//  void QQuickPopupWindow::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow20implicitWidthChangedEv(
    QQuickPopupWindow *self) {
  self->implicitWidthChanged();
}

//  void QQuickPopupWindow::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPopupWindow21implicitHeightChangedEv(
    QQuickPopupWindow *self) {
  self->implicitHeightChanged();
}

#if QT_CONFIG(wayland)
//  QRect QQuickPopupWindow::parentControlGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QQuickPopupWindow21parentControlGeometryEv(
    const QQuickPopupWindow *self) {
  return new QRect(self->parentControlGeometry());
}
#endif  // QT_CONFIG(wayland)

//  QQuickPopupWindowPrivate *QQuickPopupWindow::d_func()
extern "C" Q_DECL_EXPORT
QQuickPopupWindowPrivate *ritual_ZN17QQuickPopupWindow6d_funcEv(
    QQuickPopupWindow *self) {
  return self->d_func();
}

//  const QQuickPopupWindowPrivate *QQuickPopupWindow::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPopupWindowPrivate *ritual_ZNK17QQuickPopupWindow6d_funcEv(
    const QQuickPopupWindow *self) {
  return self->d_func();
}

//  void QQuickPopupWindow::hideEvent(QHideEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPopupWindow9hideEventEP10QHideEvent(
    QQuickPopupWindow *self,
    QHideEvent *e) {
  static_cast<OwnQQuickPopupWindow *>(self)->OwnQQuickPopupWindow::hideEvent(
      e);
}

//  void QQuickPopupWindow::moveEvent(QMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPopupWindow9moveEventEP10QMoveEvent(
    QQuickPopupWindow *self,
    QMoveEvent *e) {
  static_cast<OwnQQuickPopupWindow *>(self)->OwnQQuickPopupWindow::moveEvent(
      e);
}

//  void QQuickPopupWindow::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickPopupWindow11resizeEventEP12QResizeEvent(
    QQuickPopupWindow *self,
    QResizeEvent *e) {
  static_cast<OwnQQuickPopupWindow *>(self)->OwnQQuickPopupWindow::resizeEvent(
      e);
}

//  bool QQuickPopupWindow::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickPopupWindow5eventEP6QEvent(
    QQuickPopupWindow *self,
    QEvent *e) {
  return static_cast<OwnQQuickPopupWindow *>(self)->OwnQQuickPopupWindow::event(
      e);
}

//  a std::optional<QPoint> a ritual of QQuickPopupWindow gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickPopupWindow__std_optional_QPoint(
    std::optional<QPoint> *self) {
  delete self;
}

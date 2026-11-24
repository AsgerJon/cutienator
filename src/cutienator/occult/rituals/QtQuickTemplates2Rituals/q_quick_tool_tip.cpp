//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>

//  Only a class built on QQuickToolTip may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickToolTip : QQuickToolTip {
  using QQuickToolTip::defaultFont;
  using QQuickToolTip::itemChange;
  using QQuickToolTip::timerEvent;
  using QQuickToolTip::accessibleRole;
  using QQuickToolTip::accessibilityActiveChanged;
};

//  const QMetaObject *QQuickToolTip::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQuickToolTip10metaObjectEv(
    const QQuickToolTip *self) {
  return self->metaObject();
}

//  QString QQuickToolTip::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQuickToolTip2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickToolTip::tr(s, c, n));
}

//  void QQuickToolTip::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip21qt_qmlMarker_attachedEv(QQuickToolTip *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickToolTip::QQuickToolTip(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickToolTip *ritual_ZN13QQuickToolTipC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickToolTip(parent);
}

//  QString QQuickToolTip::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQuickToolTip4textEv(const QQuickToolTip *self) {
  return new QString(self->text());
}

//  void QQuickToolTip::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip7setTextERK7QString(
    QQuickToolTip *self,
    const QString *text) {
  self->setText(*text);
}

//  int QQuickToolTip::delay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickToolTip5delayEv(const QQuickToolTip *self) {
  return self->delay();
}

//  void QQuickToolTip::setDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip8setDelayEi(QQuickToolTip *self, int delay) {
  self->setDelay(delay);
}

//  int QQuickToolTip::timeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQuickToolTip7timeoutEv(const QQuickToolTip *self) {
  return self->timeout();
}

//  void QQuickToolTip::setTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip10setTimeoutEi(
    QQuickToolTip *self,
    int timeout) {
  self->setTimeout(timeout);
}

//  void QQuickToolTip::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip10setVisibleEb(
    QQuickToolTip *self,
    bool visible) {
  self->setVisible(visible);
}

//  QQuickToolTipAttached *QQuickToolTip::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickToolTipAttached *ritual_ZN13QQuickToolTip21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickToolTip::qmlAttachedProperties(object);
}

//  void QQuickToolTip::show(const QString &text, int ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip4showERK7QStringi(
    QQuickToolTip *self,
    const QString *text,
    int ms) {
  self->show(*text, ms);
}

//  void QQuickToolTip::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip4hideEv(QQuickToolTip *self) {
  self->hide();
}

//  QFont QQuickToolTip::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK13QQuickToolTip11defaultFontEv(const QQuickToolTip *self) {
  return new QFont(self->defaultFont());
}

//  void QQuickToolTip::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickToolTip *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickToolTip::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip10timerEventEP11QTimerEvent(
    QQuickToolTip *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickToolTip::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK13QQuickToolTip14accessibleRoleEv(
    const QQuickToolTip *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickToolTip::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQuickToolTip26accessibilityActiveChangedEb(
    QQuickToolTip *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickToolTip::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickToolTip10setVisibleEb(
    QQuickToolTip *self,
    bool visible) {
  self->QQuickToolTip::setVisible(visible);
}

//  QFont QQuickToolTip::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK13QQuickToolTip11defaultFontEv(
    const QQuickToolTip *self) {
  return new QFont(
      static_cast<const OwnQQuickToolTip *>(self)->OwnQQuickToolTip::defaultFont());
}

//  void QQuickToolTip::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickToolTip10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickToolTip *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickToolTip *>(self)->OwnQQuickToolTip::itemChange(
      change,
      *data);
}

//  void QQuickToolTip::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickToolTip10timerEventEP11QTimerEvent(
    QQuickToolTip *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickToolTip *>(self)->OwnQQuickToolTip::timerEvent(event);
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickToolTip::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK13QQuickToolTip14accessibleRoleEv(
    const QQuickToolTip *self) {
  return static_cast<const OwnQQuickToolTip *>(self)->OwnQQuickToolTip::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickToolTip::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQuickToolTip26accessibilityActiveChangedEb(
    QQuickToolTip *self,
    bool active) {
  static_cast<OwnQQuickToolTip *>(self)->OwnQQuickToolTip::accessibilityActiveChanged(
      active);
}
#endif  // QT_CONFIG(accessibility)

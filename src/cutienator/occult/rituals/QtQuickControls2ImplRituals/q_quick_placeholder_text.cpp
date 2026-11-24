//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickplaceholdertext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickplaceholdertext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickPlaceholderText may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPlaceholderText : QQuickPlaceholderText {
  using QQuickPlaceholderText::componentComplete;
};

//  const QMetaObject *QQuickPlaceholderText::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickPlaceholderText10metaObjectEv(
    const QQuickPlaceholderText *self) {
  return self->metaObject();
}

//  QString QQuickPlaceholderText::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickPlaceholderText2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPlaceholderText::tr(s, c, n));
}

//  QQuickPlaceholderText::QQuickPlaceholderText(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPlaceholderText *ritual_ZN21QQuickPlaceholderTextC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickPlaceholderText(parent);
}

//  void QQuickPlaceholderText::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPlaceholderText17componentCompleteEv(
    QQuickPlaceholderText *self) {
  self->componentComplete();
}

//  QQuickItem *QQuickPlaceholderText::textControl() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickPlaceholderText11textControlEv(
    const QQuickPlaceholderText *self) {
  return self->textControl();
}

//  void QQuickPlaceholderText::updateAlignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPlaceholderText15updateAlignmentEv(
    QQuickPlaceholderText *self) {
  self->updateAlignment();
}

//  void QQuickPlaceholderText::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickPlaceholderText17componentCompleteEv(
    QQuickPlaceholderText *self) {
  static_cast<OwnQQuickPlaceholderText *>(self)->OwnQQuickPlaceholderText::componentComplete();
}

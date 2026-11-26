//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickRow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRow : QQuickRow {
  using QQuickRow::doPositioning;
  using QQuickRow::reportConflictingAnchors;
};

//  const QMetaObject *QQuickRow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QQuickRow10metaObjectEv(
    const QQuickRow *self) {
  return self->metaObject();
}

//  void *QQuickRow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QQuickRow11qt_metacastEPKc(QQuickRow *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickRow::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QQuickRow11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickRow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickRow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QQuickRow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRow::tr(s, c, n));
}

//  QQuickRow::QQuickRow(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRow *ritual_ZN9QQuickRowC1EP10QQuickItem(QQuickItem *parent) {
  return new QQuickRow(parent);
}

//  Qt::LayoutDirection QQuickRow::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK9QQuickRow15layoutDirectionEv(
    const QQuickRow *self) {
  return self->layoutDirection();
}

//  void QQuickRow::setLayoutDirection(Qt::LayoutDirection a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickRow18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QQuickRow *self,
    Qt::LayoutDirection a0) {
  self->setLayoutDirection(a0);
}

//  Qt::LayoutDirection QQuickRow::effectiveLayoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK9QQuickRow24effectiveLayoutDirectionEv(
    const QQuickRow *self) {
  return self->effectiveLayoutDirection();
}

//  void QQuickRow::layoutDirectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickRow22layoutDirectionChangedEv(QQuickRow *self) {
  self->layoutDirectionChanged();
}

//  void QQuickRow::effectiveLayoutDirectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickRow31effectiveLayoutDirectionChangedEv(
    QQuickRow *self) {
  self->effectiveLayoutDirectionChanged();
}

//  void QQuickRow::doPositioning(QSizeF *contentSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickRow13doPositioningEP6QSizeF(
    QQuickRow *self,
    QSizeF *contentSize) {
  self->doPositioning(contentSize);
}

//  void QQuickRow::reportConflictingAnchors()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuickRow24reportConflictingAnchorsEv(QQuickRow *self) {
  self->reportConflictingAnchors();
}

//  QQuickRowPrivate *QQuickRow::d_func()
extern "C" Q_DECL_EXPORT
QQuickRowPrivate *ritual_ZN9QQuickRow6d_funcEv(QQuickRow *self) {
  return self->d_func();
}

//  const QQuickRowPrivate *QQuickRow::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRowPrivate *ritual_ZNK9QQuickRow6d_funcEv(
    const QQuickRow *self) {
  return self->d_func();
}

//  void QQuickRow::doPositioning(QSizeF *contentSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QQuickRow13doPositioningEP6QSizeF(
    QQuickRow *self,
    QSizeF *contentSize) {
  static_cast<OwnQQuickRow *>(self)->OwnQQuickRow::doPositioning(
      contentSize);
}

//  void QQuickRow::reportConflictingAnchors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QQuickRow24reportConflictingAnchorsEv(QQuickRow *self) {
  static_cast<OwnQQuickRow *>(self)->OwnQQuickRow::reportConflictingAnchors();
}

#endif  // QT_CONFIG(quick_positioners)
#endif  // QT_CONFIG(quick_positioners)

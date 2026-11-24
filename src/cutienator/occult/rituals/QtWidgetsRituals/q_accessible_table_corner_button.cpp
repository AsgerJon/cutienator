//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility) && QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessible.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>

//  QAccessibleTableCornerButton::QAccessibleTableCornerButton(QAbstractItemV
//      iew *view_)
extern "C" Q_DECL_EXPORT
QAccessibleTableCornerButton *ritual_ZN28QAccessibleTableCornerButtonC1EP17QAbstractItemView(
    QAbstractItemView *view_) {
  return new QAccessibleTableCornerButton(view_);
}

//  QObject *QAccessibleTableCornerButton::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK28QAccessibleTableCornerButton6objectEv(
    const QAccessibleTableCornerButton *self) {
  return self->object();
}

//  QAccessible::Role QAccessibleTableCornerButton::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK28QAccessibleTableCornerButton4roleEv(
    const QAccessibleTableCornerButton *self) {
  return self->role();
}

//  QAccessible::State QAccessibleTableCornerButton::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK28QAccessibleTableCornerButton5stateEv(
    const QAccessibleTableCornerButton *self) {
  return new QAccessible::State(self->state());
}

//  QRect QAccessibleTableCornerButton::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK28QAccessibleTableCornerButton4rectEv(
    const QAccessibleTableCornerButton *self) {
  return new QRect(self->rect());
}

//  bool QAccessibleTableCornerButton::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QAccessibleTableCornerButton7isValidEv(
    const QAccessibleTableCornerButton *self) {
  return self->isValid();
}

//  QAccessibleInterface *QAccessibleTableCornerButton::childAt(int a0, int
//      a1) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK28QAccessibleTableCornerButton7childAtEii(
    const QAccessibleTableCornerButton *self,
    int a0,
    int a1) {
  return self->childAt(a0, a1);
}

//  int QAccessibleTableCornerButton::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QAccessibleTableCornerButton10childCountEv(
    const QAccessibleTableCornerButton *self) {
  return self->childCount();
}

//  int QAccessibleTableCornerButton::indexOfChild(const QAccessibleInterface
//      *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QAccessibleTableCornerButton12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTableCornerButton *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QString QAccessibleTableCornerButton::text(QAccessible::Text a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QAccessibleTableCornerButton4textEN11QAccessible4TextE(
    const QAccessibleTableCornerButton *self,
    QAccessible::Text a0) {
  return new QString(self->text(a0));
}

//  void QAccessibleTableCornerButton::setText(QAccessible::Text a0, const
//      QString &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QAccessibleTableCornerButton7setTextEN11QAccessible4TextERK7QString(
    QAccessibleTableCornerButton *self,
    QAccessible::Text a0,
    const QString *a1) {
  self->setText(a0, *a1);
}

//  QAccessibleInterface *QAccessibleTableCornerButton::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK28QAccessibleTableCornerButton6parentEv(
    const QAccessibleTableCornerButton *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleTableCornerButton::child(int a0) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK28QAccessibleTableCornerButton5childEi(
    const QAccessibleTableCornerButton *self,
    int a0) {
  return self->child(a0);
}

//  QObject *QAccessibleTableCornerButton::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK28QAccessibleTableCornerButton6objectEv(
    const QAccessibleTableCornerButton *self) {
  return self->QAccessibleTableCornerButton::object();
}

//  QAccessible::Role QAccessibleTableCornerButton::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK28QAccessibleTableCornerButton4roleEv(
    const QAccessibleTableCornerButton *self) {
  return self->QAccessibleTableCornerButton::role();
}

//  QAccessible::State QAccessibleTableCornerButton::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK28QAccessibleTableCornerButton5stateEv(
    const QAccessibleTableCornerButton *self) {
  return new QAccessible::State(self->QAccessibleTableCornerButton::state());
}

//  QRect QAccessibleTableCornerButton::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK28QAccessibleTableCornerButton4rectEv(
    const QAccessibleTableCornerButton *self) {
  return new QRect(self->QAccessibleTableCornerButton::rect());
}

//  bool QAccessibleTableCornerButton::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK28QAccessibleTableCornerButton7isValidEv(
    const QAccessibleTableCornerButton *self) {
  return self->QAccessibleTableCornerButton::isValid();
}

//  QAccessibleInterface *QAccessibleTableCornerButton::childAt(int a0, int
//      a1) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK28QAccessibleTableCornerButton7childAtEii(
    const QAccessibleTableCornerButton *self,
    int a0,
    int a1) {
  return self->QAccessibleTableCornerButton::childAt(a0, a1);
}

//  int QAccessibleTableCornerButton::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QAccessibleTableCornerButton10childCountEv(
    const QAccessibleTableCornerButton *self) {
  return self->QAccessibleTableCornerButton::childCount();
}

//  int QAccessibleTableCornerButton::indexOfChild(const QAccessibleInterface
//      *a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QAccessibleTableCornerButton12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTableCornerButton *self,
    const QAccessibleInterface *a0) {
  return self->QAccessibleTableCornerButton::indexOfChild(a0);
}

//  QString QAccessibleTableCornerButton::text(QAccessible::Text a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK28QAccessibleTableCornerButton4textEN11QAccessible4TextE(
    const QAccessibleTableCornerButton *self,
    QAccessible::Text a0) {
  return new QString(self->QAccessibleTableCornerButton::text(a0));
}

//  void QAccessibleTableCornerButton::setText(QAccessible::Text a0, const
//      QString &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QAccessibleTableCornerButton7setTextEN11QAccessible4TextERK7QString(
    QAccessibleTableCornerButton *self,
    QAccessible::Text a0,
    const QString *a1) {
  self->QAccessibleTableCornerButton::setText(a0, *a1);
}

//  QAccessibleInterface *QAccessibleTableCornerButton::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK28QAccessibleTableCornerButton6parentEv(
    const QAccessibleTableCornerButton *self) {
  return self->QAccessibleTableCornerButton::parent();
}

//  QAccessibleInterface *QAccessibleTableCornerButton::child(int a0) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK28QAccessibleTableCornerButton5childEi(
    const QAccessibleTableCornerButton *self,
    int a0) {
  return self->QAccessibleTableCornerButton::child(a0);
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(accessibility) && QT_CONFIG(itemviews)

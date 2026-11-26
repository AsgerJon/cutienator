//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdayofweekrow_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdayofweekrow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickdayofweekrow_p.h>
#include <QtQuickTemplates2/private/qquickdayofweekmodel_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekrow.cpp, line 40, as local:qquickdayofweekrow.cpp:QQuickDayOfWeekRowPrivate
class QQuickDayOfWeekRowPrivate : public QQuickControlPrivate
{
public:
    QQuickDayOfWeekRowPrivate() : delegate(nullptr), model(nullptr) { }

    void resizeItems();

    QVariant source;
    QQmlComponent *delegate;
    QQuickDayOfWeekModel *model;
};

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekrow.cpp, line 52, as local:qquickdayofweekrow.cpp:QQuickDayOfWeekRowPrivate::resizeItems
inline void QQuickDayOfWeekRowPrivate::resizeItems()
{
    if (!contentItem)
        return;

    QSizeF itemSize;
    itemSize.setWidth((contentItem->width() - 6 * spacing) / 7);
    itemSize.setHeight(contentItem->height());

    const auto childItems = contentItem->childItems();
    for (QQuickItem *item : childItems)
        item->setSize(itemSize);
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekrow.cpp, line 144, as _ZN18QQuickDayOfWeekRow17componentCompleteEv
inline void QQuickDayOfWeekRow::componentComplete()
{
    Q_D(QQuickDayOfWeekRow);
    QQuickControl::componentComplete();
    d->resizeItems();
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekrow.cpp, line 151, as _ZN18QQuickDayOfWeekRow14geometryChangeERK6QRectFS2_
inline void QQuickDayOfWeekRow::geometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    Q_D(QQuickDayOfWeekRow);
    QQuickControl::geometryChange(newGeometry, oldGeometry);
    if (isComponentComplete())
        d->resizeItems();
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekrow.cpp, line 159, as _ZN18QQuickDayOfWeekRow12localeChangeERK7QLocaleS2_
inline void QQuickDayOfWeekRow::localeChange(const QLocale &newLocale, const QLocale &oldLocale)
{
    Q_D(QQuickDayOfWeekRow);
    QQuickControl::localeChange(newLocale, oldLocale);
    d->model->setLocale(newLocale);
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekrow.cpp, line 166, as _ZN18QQuickDayOfWeekRow13paddingChangeERK9QMarginsFS2_
inline void QQuickDayOfWeekRow::paddingChange(const QMarginsF &newPadding, const QMarginsF &oldPadding)
{
    Q_D(QQuickDayOfWeekRow);
    QQuickControl::paddingChange(newPadding, oldPadding);
    if (isComponentComplete())
        d->resizeItems();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickDayOfWeekRow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDayOfWeekRow : QQuickDayOfWeekRow {
  using QQuickDayOfWeekRow::componentComplete;
  using QQuickDayOfWeekRow::geometryChange;
  using QQuickDayOfWeekRow::paddingChange;
};

//  const QMetaObject *QQuickDayOfWeekRow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickDayOfWeekRow10metaObjectEv(
    const QQuickDayOfWeekRow *self) {
  return self->metaObject();
}

//  void *QQuickDayOfWeekRow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickDayOfWeekRow11qt_metacastEPKc(
    QQuickDayOfWeekRow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDayOfWeekRow::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickDayOfWeekRow11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDayOfWeekRow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickDayOfWeekRow::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDayOfWeekRow13sourceChangedEv(
    QQuickDayOfWeekRow *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickDayOfWeekRow")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickDayOfWeekRow::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDayOfWeekRow15delegateChangedEv(
    QQuickDayOfWeekRow *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickDayOfWeekRow")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "delegateChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "delegateChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickDayOfWeekRow::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDayOfWeekRow17componentCompleteEv(
    QQuickDayOfWeekRow *self) {
  self->componentComplete();
}

//  void QQuickDayOfWeekRow::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDayOfWeekRow14geometryChangeERK6QRectFS2_(
    QQuickDayOfWeekRow *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickDayOfWeekRow::localeChange(const QLocale &newLocale, const
//      QLocale &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDayOfWeekRow12localeChangeERK7QLocaleS2_(
    QQuickDayOfWeekRow *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  void QQuickDayOfWeekRow::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDayOfWeekRow13paddingChangeERK9QMarginsFS2_(
    QQuickDayOfWeekRow *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  self->paddingChange(*newPadding, *oldPadding);
}

//  QQuickDayOfWeekRowPrivate *QQuickDayOfWeekRow::d_func()
extern "C" Q_DECL_EXPORT
QQuickDayOfWeekRowPrivate *ritual_ZN18QQuickDayOfWeekRow6d_funcEv(
    QQuickDayOfWeekRow *self) {
  return self->d_func();
}

//  const QQuickDayOfWeekRowPrivate *QQuickDayOfWeekRow::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDayOfWeekRowPrivate *ritual_ZNK18QQuickDayOfWeekRow6d_funcEv(
    const QQuickDayOfWeekRow *self) {
  return self->d_func();
}

//  void QQuickDayOfWeekRow::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickDayOfWeekRow17componentCompleteEv(
    QQuickDayOfWeekRow *self) {
  static_cast<OwnQQuickDayOfWeekRow *>(self)->OwnQQuickDayOfWeekRow::componentComplete();
}

//  void QQuickDayOfWeekRow::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickDayOfWeekRow14geometryChangeERK6QRectFS2_(
    QQuickDayOfWeekRow *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickDayOfWeekRow *>(self)->OwnQQuickDayOfWeekRow::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickDayOfWeekRow::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickDayOfWeekRow13paddingChangeERK9QMarginsFS2_(
    QQuickDayOfWeekRow *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  static_cast<OwnQQuickDayOfWeekRow *>(self)->OwnQQuickDayOfWeekRow::paddingChange(
      *newPadding,
      *oldPadding);
}

#endif  // QT_CONFIG(quicktemplates2_calendar)

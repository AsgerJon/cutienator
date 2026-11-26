//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickweeknumbercolumn_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickweeknumbercolumn_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickweeknumbercolumn_p.h>
#include <QtQuickTemplates2/private/qquickweeknumbermodel_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtQml/qqmlinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbercolumn.cpp, line 42, as local:qquickweeknumbercolumn.cpp:QQuickWeekNumberColumnPrivate
class QQuickWeekNumberColumnPrivate : public QQuickControlPrivate
{
public:
    QQuickWeekNumberColumnPrivate() : delegate(nullptr), model(nullptr) { }

    void resizeItems();

    QVariant source;
    QQmlComponent *delegate;
    QQuickWeekNumberModel *model;
};

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbercolumn.cpp, line 54, as local:qquickweeknumbercolumn.cpp:QQuickWeekNumberColumnPrivate::resizeItems
inline void QQuickWeekNumberColumnPrivate::resizeItems()
{
    if (!contentItem)
        return;

    QSizeF itemSize;
    itemSize.setWidth(contentItem->width());
    itemSize.setHeight((contentItem->height() - 5 * spacing) / 6);

    const auto childItems = contentItem->childItems();
    for (QQuickItem *item : childItems)
        item->setSize(itemSize);
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbercolumn.cpp, line 184, as _ZN22QQuickWeekNumberColumn17componentCompleteEv
inline void QQuickWeekNumberColumn::componentComplete()
{
    Q_D(QQuickWeekNumberColumn);
    QQuickControl::componentComplete();
    d->resizeItems();
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbercolumn.cpp, line 191, as _ZN22QQuickWeekNumberColumn14geometryChangeERK6QRectFS2_
inline void QQuickWeekNumberColumn::geometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    Q_D(QQuickWeekNumberColumn);
    QQuickControl::geometryChange(newGeometry, oldGeometry);
    if (isComponentComplete())
        d->resizeItems();
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbercolumn.cpp, line 199, as _ZN22QQuickWeekNumberColumn12localeChangeERK7QLocaleS2_
inline void QQuickWeekNumberColumn::localeChange(const QLocale &newLocale, const QLocale &oldLocale)
{
    Q_D(QQuickWeekNumberColumn);
    QQuickControl::localeChange(newLocale, oldLocale);
    d->model->setLocale(newLocale);
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbercolumn.cpp, line 206, as _ZN22QQuickWeekNumberColumn13paddingChangeERK9QMarginsFS2_
inline void QQuickWeekNumberColumn::paddingChange(const QMarginsF &newPadding, const QMarginsF &oldPadding)
{
    Q_D(QQuickWeekNumberColumn);
    QQuickControl::paddingChange(newPadding, oldPadding);
    if (isComponentComplete())
        d->resizeItems();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickWeekNumberColumn may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWeekNumberColumn : QQuickWeekNumberColumn {
  using QQuickWeekNumberColumn::componentComplete;
  using QQuickWeekNumberColumn::geometryChange;
  using QQuickWeekNumberColumn::paddingChange;
};

//  const QMetaObject *QQuickWeekNumberColumn::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickWeekNumberColumn10metaObjectEv(
    const QQuickWeekNumberColumn *self) {
  return self->metaObject();
}

//  void *QQuickWeekNumberColumn::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickWeekNumberColumn11qt_metacastEPKc(
    QQuickWeekNumberColumn *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWeekNumberColumn::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickWeekNumberColumn11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWeekNumberColumn *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickWeekNumberColumn::monthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWeekNumberColumn12monthChangedEv(
    QQuickWeekNumberColumn *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberColumn")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "monthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "monthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickWeekNumberColumn::yearChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWeekNumberColumn11yearChangedEv(
    QQuickWeekNumberColumn *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberColumn")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "yearChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "yearChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickWeekNumberColumn::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWeekNumberColumn13sourceChangedEv(
    QQuickWeekNumberColumn *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberColumn")) {
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

//  void QQuickWeekNumberColumn::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWeekNumberColumn15delegateChangedEv(
    QQuickWeekNumberColumn *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberColumn")) {
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

//  void QQuickWeekNumberColumn::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWeekNumberColumn17componentCompleteEv(
    QQuickWeekNumberColumn *self) {
  self->componentComplete();
}

//  void QQuickWeekNumberColumn::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWeekNumberColumn14geometryChangeERK6QRectFS2_(
    QQuickWeekNumberColumn *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickWeekNumberColumn::localeChange(const QLocale &newLocale, const
//      QLocale &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWeekNumberColumn12localeChangeERK7QLocaleS2_(
    QQuickWeekNumberColumn *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  void QQuickWeekNumberColumn::paddingChange(const QMarginsF &newPadding,
//      const QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickWeekNumberColumn13paddingChangeERK9QMarginsFS2_(
    QQuickWeekNumberColumn *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  self->paddingChange(*newPadding, *oldPadding);
}

//  QQuickWeekNumberColumnPrivate *QQuickWeekNumberColumn::d_func()
extern "C" Q_DECL_EXPORT
QQuickWeekNumberColumnPrivate *ritual_ZN22QQuickWeekNumberColumn6d_funcEv(
    QQuickWeekNumberColumn *self) {
  return self->d_func();
}

//  const QQuickWeekNumberColumnPrivate *QQuickWeekNumberColumn::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickWeekNumberColumnPrivate *ritual_ZNK22QQuickWeekNumberColumn6d_funcEv(
    const QQuickWeekNumberColumn *self) {
  return self->d_func();
}

//  void QQuickWeekNumberColumn::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickWeekNumberColumn17componentCompleteEv(
    QQuickWeekNumberColumn *self) {
  static_cast<OwnQQuickWeekNumberColumn *>(self)->OwnQQuickWeekNumberColumn::componentComplete();
}

//  void QQuickWeekNumberColumn::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickWeekNumberColumn14geometryChangeERK6QRectFS2_(
    QQuickWeekNumberColumn *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickWeekNumberColumn *>(self)->OwnQQuickWeekNumberColumn::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickWeekNumberColumn::paddingChange(const QMarginsF &newPadding,
//      const QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickWeekNumberColumn13paddingChangeERK9QMarginsFS2_(
    QQuickWeekNumberColumn *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  static_cast<OwnQQuickWeekNumberColumn *>(self)->OwnQQuickWeekNumberColumn::paddingChange(
      *newPadding,
      *oldPadding);
}

#endif  // QT_CONFIG(quicktemplates2_calendar)

//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmonthgrid_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmonthgrid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickmonthgrid_p.h>
#include <QtQuickTemplates2/private/qquickmonthmodel_p.h>
#include <QtGui/qstylehints.h>
#include <QtGui/qguiapplication.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtQml/qqmlinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 79, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate
class QQuickMonthGridPrivate : public QQuickControlPrivate
{
    Q_DECLARE_PUBLIC(QQuickMonthGrid)

public:
    QQuickMonthGridPrivate() : pressTimer(0), pressedItem(nullptr), model(nullptr), delegate(nullptr) { }

    void resizeItems();

    QQuickItem *cellAt(const QPointF &pos) const;
    QDateTime dateOf(QQuickItem *cell) const;

    void updatePress(const QPointF &pos);
    void clearPress(bool clicked);

    bool handlePress(const QPointF &point, ulong timestamp) override;
    bool handleMove(const QPointF &point, ulong timestamp) override;
    bool handleRelease(const QPointF &point, ulong timestamp) override;
    void handleUngrab() override;

    QString title;
    QVariant source;

    // Only the date matters, but we have to store it as QDateTime for compatibility
    // with Date: QTBUG-72208. See QQuickMonthModelPrivate::populate for more info.
    QDateTime pressedDate;
    int pressTimer;
    QQuickItem *pressedItem;
    QQuickMonthModel *model;
    QQmlComponent *delegate;
};

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 111, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::resizeItems
inline void QQuickMonthGridPrivate::resizeItems()
{
    if (!contentItem)
        return;

    QSizeF itemSize;
    itemSize.setWidth((contentItem->width() - 6 * spacing) / 7);
    itemSize.setHeight((contentItem->height() - 5 * spacing) / 6);

    const auto childItems = contentItem->childItems();
    for (QQuickItem *item : childItems) {
        if (!QQuickItemPrivate::get(item)->isTransparentForPositioner())
            item->setSize(itemSize);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 127, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::cellAt
inline QQuickItem *QQuickMonthGridPrivate::cellAt(const QPointF &pos) const
{
    Q_Q(const QQuickMonthGrid);
    if (contentItem) {
        QPointF mapped = q->mapToItem(contentItem, pos);
        return contentItem->childAt(mapped.x(), mapped.y());
    }
    return nullptr;
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 137, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::dateOf
inline QDateTime QQuickMonthGridPrivate::dateOf(QQuickItem *cell) const
{
    if (contentItem)
        return model->dateAt(contentItem->childItems().indexOf(cell));
    return {};
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 144, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::updatePress
inline void QQuickMonthGridPrivate::updatePress(const QPointF &pos)
{
    Q_Q(QQuickMonthGrid);
    clearPress(false);
    pressedItem = cellAt(pos);
    pressedDate = dateOf(pressedItem);
    if (pressedDate.isValid())
        emit q->pressed(pressedDate);
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 154, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::clearPress
inline void QQuickMonthGridPrivate::clearPress(bool clicked)
{
    Q_Q(QQuickMonthGrid);
    if (pressedDate.isValid()) {
        emit q->released(pressedDate);
        if (clicked)
            emit q->clicked(pressedDate);
    }
    pressedDate = {};
    pressedItem = nullptr;
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 166, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::handlePress
inline bool QQuickMonthGridPrivate::handlePress(const QPointF &point, ulong timestamp)
{
    Q_Q(QQuickMonthGrid);
    QQuickControlPrivate::handlePress(point, timestamp);
    updatePress(point);
    if (pressedDate.isValid())
        pressTimer = q->startTimer(qGuiApp->styleHints()->mousePressAndHoldInterval());
    return true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 176, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::handleMove
inline bool QQuickMonthGridPrivate::handleMove(const QPointF &point, ulong timestamp)
{
    QQuickControlPrivate::handleMove(point, timestamp);
    updatePress(point);
    return true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 183, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::handleRelease
inline bool QQuickMonthGridPrivate::handleRelease(const QPointF &point, ulong timestamp)
{
    QQuickControlPrivate::handleRelease(point, timestamp);
    clearPress(true);
    return true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 190, as local:qquickmonthgrid.cpp:QQuickMonthGridPrivate::handleUngrab
inline void QQuickMonthGridPrivate::handleUngrab()
{
    QQuickControlPrivate::handleUngrab();
    clearPress(false);
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthmodel.cpp, line 12, as local:qquickmonthmodel.cpp:daysInAWeek
namespace {
static const int daysInAWeek = 7;
}  // namespace

//  from ../qtdeclarative/src/quicktemplates/qquickmonthmodel.cpp, line 13, as local:qquickmonthmodel.cpp:weeksOnACalendarMonth
namespace {
static const int weeksOnACalendarMonth = 6;
}  // namespace

//  from ../qtdeclarative/src/quicktemplates/qquickmonthmodel.cpp, line 14, as local:qquickmonthmodel.cpp:daysOnACalendarMonth
namespace {
static const int daysOnACalendarMonth = daysInAWeek * weeksOnACalendarMonth;
}  // namespace

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 351, as _ZN15QQuickMonthGrid17componentCompleteEv
inline void QQuickMonthGrid::componentComplete()
{
    Q_D(QQuickMonthGrid);
    QQuickControl::componentComplete();
    d->resizeItems();
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 358, as _ZN15QQuickMonthGrid14geometryChangeERK6QRectFS2_
inline void QQuickMonthGrid::geometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    Q_D(QQuickMonthGrid);
    QQuickControl::geometryChange(newGeometry, oldGeometry);
    if (isComponentComplete())
        d->resizeItems();
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 366, as _ZN15QQuickMonthGrid12localeChangeERK7QLocaleS2_
inline void QQuickMonthGrid::localeChange(const QLocale &newLocale, const QLocale &oldLocale)
{
    Q_D(QQuickMonthGrid);
    QQuickControl::localeChange(newLocale, oldLocale);
    d->model->setLocale(newLocale);
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 373, as _ZN15QQuickMonthGrid13paddingChangeERK9QMarginsFS2_
inline void QQuickMonthGrid::paddingChange(const QMarginsF &newPadding, const QMarginsF &oldPadding)
{
    Q_D(QQuickMonthGrid);
    QQuickControl::paddingChange(newPadding, oldPadding);
    if (isComponentComplete())
        d->resizeItems();
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 381, as _ZN15QQuickMonthGrid12updatePolishEv
inline void QQuickMonthGrid::updatePolish()
{
    Q_D(QQuickMonthGrid);
    QQuickControl::updatePolish();
    d->resizeItems();
}

//  from ../qtdeclarative/src/quicktemplates/qquickmonthgrid.cpp, line 388, as _ZN15QQuickMonthGrid10timerEventEP11QTimerEvent
inline void QQuickMonthGrid::timerEvent(QTimerEvent *event)
{
    Q_D(QQuickMonthGrid);
    if (event->timerId() == d->pressTimer) {
        if (d->pressedDate.isValid())
            emit pressAndHold(d->pressedDate);
        killTimer(d->pressTimer);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickMonthGrid may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMonthGrid : QQuickMonthGrid {
  using QQuickMonthGrid::componentComplete;
  using QQuickMonthGrid::geometryChange;
  using QQuickMonthGrid::paddingChange;
  using QQuickMonthGrid::updatePolish;
};

//  const QMetaObject *QQuickMonthGrid::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickMonthGrid10metaObjectEv(
    const QQuickMonthGrid *self) {
  return self->metaObject();
}

//  void *QQuickMonthGrid::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickMonthGrid11qt_metacastEPKc(
    QQuickMonthGrid *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMonthGrid::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickMonthGrid11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMonthGrid *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickMonthGrid::monthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid12monthChangedEv(QQuickMonthGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
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

//  void QQuickMonthGrid::yearChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid11yearChangedEv(QQuickMonthGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
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

//  void QQuickMonthGrid::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid13sourceChangedEv(QQuickMonthGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
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

//  void QQuickMonthGrid::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid12titleChangedEv(QQuickMonthGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "titleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "titleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickMonthGrid::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid15delegateChangedEv(QQuickMonthGrid *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
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

//  void QQuickMonthGrid::pressed(QDateTime date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid7pressedE9QDateTime(
    QQuickMonthGrid *self,
    const QDateTime *date) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pressed(QDateTime)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pressed(QDateTime)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(date)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickMonthGrid::released(QDateTime date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid8releasedE9QDateTime(
    QQuickMonthGrid *self,
    const QDateTime *date) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "released(QDateTime)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "released(QDateTime)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(date)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickMonthGrid::clicked(QDateTime date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid7clickedE9QDateTime(
    QQuickMonthGrid *self,
    const QDateTime *date) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clicked(QDateTime)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clicked(QDateTime)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(date)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickMonthGrid::pressAndHold(QDateTime date)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid12pressAndHoldE9QDateTime(
    QQuickMonthGrid *self,
    const QDateTime *date) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickMonthGrid")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pressAndHold(QDateTime)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pressAndHold(QDateTime)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(date)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickMonthGrid::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid17componentCompleteEv(QQuickMonthGrid *self) {
  self->componentComplete();
}

//  void QQuickMonthGrid::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid14geometryChangeERK6QRectFS2_(
    QQuickMonthGrid *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickMonthGrid::localeChange(const QLocale &newLocale, const
//      QLocale &oldLocale)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid12localeChangeERK7QLocaleS2_(
    QQuickMonthGrid *self,
    const QLocale *newLocale,
    const QLocale *oldLocale) {
  self->localeChange(*newLocale, *oldLocale);
}

//  void QQuickMonthGrid::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid13paddingChangeERK9QMarginsFS2_(
    QQuickMonthGrid *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  self->paddingChange(*newPadding, *oldPadding);
}

//  void QQuickMonthGrid::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid12updatePolishEv(QQuickMonthGrid *self) {
  self->updatePolish();
}

//  void QQuickMonthGrid::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMonthGrid10timerEventEP11QTimerEvent(
    QQuickMonthGrid *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QQuickMonthGridPrivate *QQuickMonthGrid::d_func()
extern "C" Q_DECL_EXPORT
QQuickMonthGridPrivate *ritual_ZN15QQuickMonthGrid6d_funcEv(
    QQuickMonthGrid *self) {
  return self->d_func();
}

//  const QQuickMonthGridPrivate *QQuickMonthGrid::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMonthGridPrivate *ritual_ZNK15QQuickMonthGrid6d_funcEv(
    const QQuickMonthGrid *self) {
  return self->d_func();
}

//  void QQuickMonthGrid::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMonthGrid17componentCompleteEv(
    QQuickMonthGrid *self) {
  static_cast<OwnQQuickMonthGrid *>(self)->OwnQQuickMonthGrid::componentComplete();
}

//  void QQuickMonthGrid::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMonthGrid14geometryChangeERK6QRectFS2_(
    QQuickMonthGrid *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickMonthGrid *>(self)->OwnQQuickMonthGrid::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickMonthGrid::paddingChange(const QMarginsF &newPadding, const
//      QMarginsF &oldPadding)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMonthGrid13paddingChangeERK9QMarginsFS2_(
    QQuickMonthGrid *self,
    const QMarginsF *newPadding,
    const QMarginsF *oldPadding) {
  static_cast<OwnQQuickMonthGrid *>(self)->OwnQQuickMonthGrid::paddingChange(
      *newPadding,
      *oldPadding);
}

//  void QQuickMonthGrid::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickMonthGrid12updatePolishEv(QQuickMonthGrid *self) {
  static_cast<OwnQQuickMonthGrid *>(self)->OwnQQuickMonthGrid::updatePolish();
}

#endif  // QT_CONFIG(quicktemplates2_calendar)

//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickcalendarmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcalendarmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickcalendarmodel_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 36, as local:qquickcalendarmodel.cpp:QQuickCalendarModelPrivate
class QQuickCalendarModelPrivate : public QAbstractItemModelPrivate
{
    Q_DECLARE_PUBLIC(QQuickCalendarModel)

public:
    QQuickCalendarModelPrivate() : complete(false),
        from(1,1,1), to(275759, 9, 25), count(0)
    {
    }

    static int getCount(QDate from, QDate to);

    void populate(QDate from, QDate to, bool force = false);

    bool complete;
    QDate from;
    QDate to;
    int count;
};

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 58, as local:qquickcalendarmodel.cpp:QQuickCalendarModelPrivate::getCount
inline int QQuickCalendarModelPrivate::getCount(QDate from, QDate to)
{
    if (!from.isValid() || !to.isValid())
        return 0;

    const QCalendar gregorian;
    Q_ASSERT(gregorian.isGregorian());
    const QCalendar::YearMonthDay &f = gregorian.partsFromDate(from);
    const QCalendar::YearMonthDay &t = gregorian.partsFromDate(to);
    Q_ASSERT(f.isValid() && t.isValid()); // ... because from and to are valid.
    if (f.year > t.year || (f.year == t.year && f.month > t.month))
        return 0;

    // Count from's month and every subsequent month until to's:
    return 1 + t.month + 12 * (t.year - f.year) - f.month;
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 75, as local:qquickcalendarmodel.cpp:QQuickCalendarModelPrivate::populate
inline void QQuickCalendarModelPrivate::populate(QDate f, QDate t, bool force)
{
    Q_Q(QQuickCalendarModel);
    if (!force && f == from && t == to)
        return;

    int c = getCount(f, t);
    if (c != count) {
        q->beginResetModel();
        count = c;
        q->endResetModel();
        emit q->countChanged();
    } else {
        emit q->dataChanged(q->index(0, 0), q->index(c - 1, 0));
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 168, as _ZNK19QQuickCalendarModel7indexOfE5QDate
inline int QQuickCalendarModel::indexOf(QDate date) const
{
    Q_D(const QQuickCalendarModel);
    return d->getCount(d->from, date) - 1;
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 184, as _ZNK19QQuickCalendarModel4dataERK11QModelIndexi
inline QVariant QQuickCalendarModel::data(const QModelIndex &index, int role) const
{
    Q_D(const QQuickCalendarModel);
    if (index.isValid() && index.row() < d->count) {
        switch (role) {
        case MonthRole:
            return monthAt(index.row());
        case YearRole:
            return yearAt(index.row());
        default:
            break;
        }
    }
    return QVariant();
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 200, as _ZNK19QQuickCalendarModel8rowCountERK11QModelIndex
inline int QQuickCalendarModel::rowCount(const QModelIndex &parent) const
{
    Q_D(const QQuickCalendarModel);
    if (!parent.isValid())
        return d->count;
    return 0;
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 216, as _ZN19QQuickCalendarModel10classBeginEv
inline void QQuickCalendarModel::classBegin()
{
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 220, as _ZN19QQuickCalendarModel17componentCompleteEv
inline void QQuickCalendarModel::componentComplete()
{
    Q_D(QQuickCalendarModel);
    d->complete = true;
    d->populate(d->from, d->to, true);
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 157, as _ZNK19QQuickCalendarModel6yearAtEi
inline int QQuickCalendarModel::yearAt(int index) const
{
    Q_D(const QQuickCalendarModel);
    return d->from.addMonths(index).year();
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 146, as _ZNK19QQuickCalendarModel7monthAtEi
inline int QQuickCalendarModel::monthAt(int index) const
{
    Q_D(const QQuickCalendarModel);
    return d->from.addMonths(index).month() - 1;
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 179, as _ZNK19QQuickCalendarModel7indexOfEii
inline int QQuickCalendarModel::indexOf(int year, int month) const
{
    return indexOf(QDate(year, month + 1, 1));
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickCalendarModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickCalendarModel : QQuickCalendarModel {
  using QQuickCalendarModel::classBegin;
};

//  const QMetaObject *QQuickCalendarModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickCalendarModel10metaObjectEv(
    const QQuickCalendarModel *self) {
  return self->metaObject();
}

//  void *QQuickCalendarModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickCalendarModel11qt_metacastEPKc(
    QQuickCalendarModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickCalendarModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickCalendarModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickCalendarModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  int QQuickCalendarModel::indexOf(int year, int month) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickCalendarModel7indexOfEii(
    const QQuickCalendarModel *self,
    int year,
    int month) {
  return self->indexOf(year, month);
}

//  QHash<int, QByteArray> QQuickCalendarModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK19QQuickCalendarModel9roleNamesEv(
    const QQuickCalendarModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QQuickCalendarModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickCalendarModel4dataERK11QModelIndexi(
    const QQuickCalendarModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  int QQuickCalendarModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuickCalendarModel8rowCountERK11QModelIndex(
    const QQuickCalendarModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  void QQuickCalendarModel::fromChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCalendarModel11fromChangedEv(
    QQuickCalendarModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickCalendarModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fromChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fromChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickCalendarModel::toChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCalendarModel9toChangedEv(QQuickCalendarModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickCalendarModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "toChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "toChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickCalendarModel::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCalendarModel12countChangedEv(
    QQuickCalendarModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickCalendarModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "countChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "countChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickCalendarModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCalendarModel10classBeginEv(
    QQuickCalendarModel *self) {
  self->classBegin();
}

//  void QQuickCalendarModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCalendarModel17componentCompleteEv(
    QQuickCalendarModel *self) {
  self->componentComplete();
}

//  QQuickCalendarModelPrivate *QQuickCalendarModel::d_func()
extern "C" Q_DECL_EXPORT
QQuickCalendarModelPrivate *ritual_ZN19QQuickCalendarModel6d_funcEv(
    QQuickCalendarModel *self) {
  return self->d_func();
}

//  const QQuickCalendarModelPrivate *QQuickCalendarModel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickCalendarModelPrivate *ritual_ZNK19QQuickCalendarModel6d_funcEv(
    const QQuickCalendarModel *self) {
  return self->d_func();
}

//  QQuickCalendarModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickCalendarModel_QQmlParserStatus(
    QQuickCalendarModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  QVariant QQuickCalendarModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QQuickCalendarModel4dataERK11QModelIndexi(
    const QQuickCalendarModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQuickCalendarModel::data(*index, role));
}

//  int QQuickCalendarModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QQuickCalendarModel8rowCountERK11QModelIndex(
    const QQuickCalendarModel *self,
    const QModelIndex *parent) {
  return self->QQuickCalendarModel::rowCount(*parent);
}

//  void QQuickCalendarModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickCalendarModel10classBeginEv(
    QQuickCalendarModel *self) {
  static_cast<OwnQQuickCalendarModel *>(self)->OwnQQuickCalendarModel::classBegin();
}

#endif  // QT_CONFIG(quicktemplates2_calendar)

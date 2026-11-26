//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickweeknumbermodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickweeknumbermodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickweeknumbermodel_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/qdatetime.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 12, as local:qquickweeknumbermodel.cpp:QQuickWeekNumberModelPrivate
class QQuickWeekNumberModelPrivate : public QAbstractItemModelPrivate
{
    Q_DECLARE_PUBLIC(QQuickWeekNumberModel)

public:
    QQuickWeekNumberModelPrivate() : month(-1), year(-1), weekNumbers{}
    {
        QDate date = QDate::currentDate();
        init(date.month(), date.year(), locale);
        month = date.month();
        year = date.year();
    }

    void init(int month, int year, const QLocale &locale = QLocale());
    static QDate calculateFirst(int month, int year, const QLocale &locale);

    int month;
    int year;
    QLocale locale;
    int weekNumbers[6];
};

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 34, as local:qquickweeknumbermodel.cpp:QQuickWeekNumberModelPrivate::init
inline void QQuickWeekNumberModelPrivate::init(int m, int y, const QLocale &l)
{
    Q_Q(QQuickWeekNumberModel);
    if (m == month && y == year && l.firstDayOfWeek() == locale.firstDayOfWeek())
        return;

    // The actual first (1st) day of the month.
    QDate firstDayOfMonthDate(y, m, 1);
    int difference = ((firstDayOfMonthDate.dayOfWeek() - l.firstDayOfWeek()) + 7) % 7;
    // The first day to display should never be the 1st of the month, as we want some days from
    // the previous month to be visible.
    if (difference == 0)
        difference += 7;

    for (int i = 0; i < 6; ++i)
        weekNumbers[i] = firstDayOfMonthDate.addDays(i * 7 - difference).weekNumber();

    if (q) // null at construction
        emit q->dataChanged(q->index(0, 0), q->index(5, 0));
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 124, as _ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi
inline QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int role) const
{
    if (role == WeekNumberRole) {
        int weekNumber = weekNumberAt(index.row());
        if (weekNumber != -1)
            return weekNumber;
    }
    return QVariant();
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 134, as _ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex
inline int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid())
        return 0;
    return 6;
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 108, as _ZNK21QQuickWeekNumberModel12weekNumberAtEi
inline int QQuickWeekNumberModel::weekNumberAt(int index) const
{
    Q_D(const QQuickWeekNumberModel);
    if (index < 0 || index > 5)
        return -1;
    return d->weekNumbers[index];
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickWeekNumberModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickWeekNumberModel10metaObjectEv(
    const QQuickWeekNumberModel *self) {
  return self->metaObject();
}

//  void *QQuickWeekNumberModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickWeekNumberModel11qt_metacastEPKc(
    QQuickWeekNumberModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWeekNumberModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickWeekNumberModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWeekNumberModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QHash<int, QByteArray> QQuickWeekNumberModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK21QQuickWeekNumberModel9roleNamesEv(
    const QQuickWeekNumberModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi(
    const QQuickWeekNumberModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex(
    const QQuickWeekNumberModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  void QQuickWeekNumberModel::monthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWeekNumberModel12monthChangedEv(
    QQuickWeekNumberModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberModel")) {
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

//  void QQuickWeekNumberModel::yearChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWeekNumberModel11yearChangedEv(
    QQuickWeekNumberModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberModel")) {
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

//  void QQuickWeekNumberModel::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickWeekNumberModel13localeChangedEv(
    QQuickWeekNumberModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickWeekNumberModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "localeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "localeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuickWeekNumberModelPrivate *QQuickWeekNumberModel::d_func()
extern "C" Q_DECL_EXPORT
QQuickWeekNumberModelPrivate *ritual_ZN21QQuickWeekNumberModel6d_funcEv(
    QQuickWeekNumberModel *self) {
  return self->d_func();
}

//  const QQuickWeekNumberModelPrivate *QQuickWeekNumberModel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWeekNumberModelPrivate *ritual_ZNK21QQuickWeekNumberModel6d_funcEv(
    const QQuickWeekNumberModel *self) {
  return self->d_func();
}

//  QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi(
    const QQuickWeekNumberModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQuickWeekNumberModel::data(*index, role));
}

//  int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex(
    const QQuickWeekNumberModel *self,
    const QModelIndex *parent) {
  return self->QQuickWeekNumberModel::rowCount(*parent);
}

#endif  // QT_CONFIG(quicktemplates2_calendar)

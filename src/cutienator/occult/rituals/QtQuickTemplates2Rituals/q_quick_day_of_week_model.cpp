//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdayofweekmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdayofweekmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickdayofweekmodel_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 11, as local:qquickdayofweekmodel.cpp:QQuickDayOfWeekModelPrivate
class QQuickDayOfWeekModelPrivate : public QAbstractItemModelPrivate
{
    Q_DECLARE_PUBLIC(QQuickDayOfWeekModel)

public:
    QLocale locale;
};

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 51, as _ZNK20QQuickDayOfWeekModel4dataERK11QModelIndexi
inline QVariant QQuickDayOfWeekModel::data(const QModelIndex &index, int role) const
{
    Q_D(const QQuickDayOfWeekModel);
    if (index.isValid() && index.row() < 7) {
        int day = dayAt(index.row());
        switch (role) {
        case DayRole:
            return day;
        case LongNameRole:
            return d->locale.standaloneDayName(day == 0 ? Qt::Sunday : day, QLocale::LongFormat);
        case ShortNameRole:
            return d->locale.standaloneDayName(day == 0 ? Qt::Sunday : day, QLocale::ShortFormat);
        case NarrowNameRole:
            return d->locale.standaloneDayName(day == 0 ? Qt::Sunday : day, QLocale::NarrowFormat);
        default:
            break;
        }
    }
    return QVariant();
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 72, as _ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex
inline int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid())
        return 0;
    return 7;
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 40, as _ZNK20QQuickDayOfWeekModel5dayAtEi
inline int QQuickDayOfWeekModel::dayAt(int index) const
{
    Q_D(const QQuickDayOfWeekModel);
    int day = d->locale.firstDayOfWeek() + index;
    if (day > 7)
        day -= 7;
    if (day == 7)
        day = 0; // Qt::Sunday = 7, but Sunday is 0 in JS Date
    return day;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickDayOfWeekModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickDayOfWeekModel10metaObjectEv(
    const QQuickDayOfWeekModel *self) {
  return self->metaObject();
}

//  void *QQuickDayOfWeekModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickDayOfWeekModel11qt_metacastEPKc(
    QQuickDayOfWeekModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDayOfWeekModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickDayOfWeekModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDayOfWeekModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QHash<int, QByteArray> QQuickDayOfWeekModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK20QQuickDayOfWeekModel9roleNamesEv(
    const QQuickDayOfWeekModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QQuickDayOfWeekModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QQuickDayOfWeekModel4dataERK11QModelIndexi(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  void QQuickDayOfWeekModel::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickDayOfWeekModel13localeChangedEv(
    QQuickDayOfWeekModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickDayOfWeekModel")) {
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

//  QQuickDayOfWeekModelPrivate *QQuickDayOfWeekModel::d_func()
extern "C" Q_DECL_EXPORT
QQuickDayOfWeekModelPrivate *ritual_ZN20QQuickDayOfWeekModel6d_funcEv(
    QQuickDayOfWeekModel *self) {
  return self->d_func();
}

//  const QQuickDayOfWeekModelPrivate *QQuickDayOfWeekModel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickDayOfWeekModelPrivate *ritual_ZNK20QQuickDayOfWeekModel6d_funcEv(
    const QQuickDayOfWeekModel *self) {
  return self->d_func();
}

//  QVariant QQuickDayOfWeekModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QQuickDayOfWeekModel4dataERK11QModelIndexi(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQuickDayOfWeekModel::data(*index, role));
}

//  int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *parent) {
  return self->QQuickDayOfWeekModel::rowCount(*parent);
}

#endif  // QT_CONFIG(quicktemplates2_calendar)

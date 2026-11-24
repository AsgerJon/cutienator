//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbustraytypes_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(systemtrayicon)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbustraytypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QXdgDBusImageStruct::QXdgDBusImageStruct()
extern "C" Q_DECL_EXPORT
QXdgDBusImageStruct *ritual_ZN19QXdgDBusImageStructC1Ev() {
  return new QXdgDBusImageStruct();
}

//  QXdgDBusImageStruct::QXdgDBusImageStruct(int w, int h)
extern "C" Q_DECL_EXPORT
QXdgDBusImageStruct *ritual_ZN19QXdgDBusImageStructC1Eii(int w, int h) {
  return new QXdgDBusImageStruct(w, h);
}

//  QXdgDBusImageStruct::~QXdgDBusImageStruct()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QXdgDBusImageStructD1Ev(QXdgDBusImageStruct *self) {
  delete self;
}

//  QList<QXdgDBusImageStruct>::QList()
extern "C" Q_DECL_EXPORT
QList<QXdgDBusImageStruct> *ritual_list_make_QXdgDBusImageStruct() {
  return new QList<QXdgDBusImageStruct>();
}

//  void QList<QXdgDBusImageStruct>::append(const QXdgDBusImageStruct &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QXdgDBusImageStruct(
    QList<QXdgDBusImageStruct> *self,
    const QXdgDBusImageStruct *element) {
  self->append(*element);
}

//  qsizetype QList<QXdgDBusImageStruct>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QXdgDBusImageStruct(
    const QList<QXdgDBusImageStruct> *self) {
  return self->size();
}

//  const QXdgDBusImageStruct &QList<QXdgDBusImageStruct>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QXdgDBusImageStruct *ritual_list_at_QXdgDBusImageStruct(
    const QList<QXdgDBusImageStruct> *self,
    long long index) {
  return new QXdgDBusImageStruct(self->at(index));
}

//  QList<QXdgDBusImageStruct>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QXdgDBusImageStruct(QList<QXdgDBusImageStruct> *self) {
  delete self;
}

#endif  // QT_CONFIG(systemtrayicon)

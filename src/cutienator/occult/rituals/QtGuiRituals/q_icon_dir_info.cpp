//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qiconloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QIconDirInfo::QIconDirInfo(const QString &_path)
extern "C" Q_DECL_EXPORT
QIconDirInfo *ritual_ZN12QIconDirInfoC1ERK7QString(const QString *_path) {
  return new QIconDirInfo(*_path);
}

//  QIconDirInfo::~QIconDirInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIconDirInfoD1Ev(QIconDirInfo *self) {
  delete self;
}

//  QList<QIconDirInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QIconDirInfo> *ritual_list_make_QIconDirInfo() {
  return new QList<QIconDirInfo>();
}

//  void QList<QIconDirInfo>::append(const QIconDirInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QIconDirInfo(
    QList<QIconDirInfo> *self,
    const QIconDirInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QIconDirInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QIconDirInfo(const QList<QIconDirInfo> *self) {
  return self->size();
}

//  const QIconDirInfo &QList<QIconDirInfo>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QIconDirInfo *ritual_list_at_QIconDirInfo(
    const QList<QIconDirInfo> *self,
    long long index) {
  return new QIconDirInfo(self->at(index));
}

//  QList<QIconDirInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QIconDirInfo(QList<QIconDirInfo> *self) {
  delete self;
}

#endif  // !defined(QT_NO_ICON)

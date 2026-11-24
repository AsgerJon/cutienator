//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qresource_iterator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qresource_iterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qresource.h"
#include "qresource_iterator_p.h"
#include <QtCore/qvariant.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qresource_iterator.cpp, line 12, as _ZN27QResourceFileEngineIteratorC1ERK7QString6QFlagsIN4QDir6FilterEERK5QListIS0_E
inline QResourceFileEngineIterator::QResourceFileEngineIterator(const QString &path, QDir::Filters filters,
                                                         const QStringList &filterNames)
    : QAbstractFileEngineIterator(path, filters, filterNames),
      index(-1)
{
}

//  from src/corelib/io/qresource_iterator.cpp, line 19, as _ZN27QResourceFileEngineIteratorC1ERK7QString6QFlagsIN11QDirListing12IteratorFlagEERK5QListIS0_E
inline QResourceFileEngineIterator::QResourceFileEngineIterator(const QString &path,
                                                         QDirListing::IteratorFlags filters,
                                                         const QStringList &filterNames)
    : QAbstractFileEngineIterator(path, filters, filterNames),
      index(-1)
{
}

//  from src/corelib/io/qresource_iterator.cpp, line 27, as _ZN27QResourceFileEngineIteratorD1Ev
inline QResourceFileEngineIterator::~QResourceFileEngineIterator()
{
}

//  from src/corelib/io/qresource_iterator.cpp, line 31, as _ZN27QResourceFileEngineIterator7advanceEv
inline bool QResourceFileEngineIterator::advance()
{
    if (index == -1) {
        // Lazy initialization of the iterator
        QResource resource(path());
        if (!resource.isValid())
            return false;

        // Initialize and move to the first entry.
        entries = resource.children();
        if (entries.isEmpty())
            return false;

        index = 0;
        return true;
    }

    if (index < entries.size() - 1) {
        ++index;
        return true;
    }

    return false;
}

//  from src/corelib/io/qresource_iterator.cpp, line 56, as _ZNK27QResourceFileEngineIterator15currentFileNameEv
inline QString QResourceFileEngineIterator::currentFileName() const
{
    if (index < 0 || index > entries.size())
        return QString();
    return entries.at(index);
}

//  from src/corelib/io/qresource_iterator.cpp, line 63, as _ZNK27QResourceFileEngineIterator15currentFileInfoEv
inline QFileInfo QResourceFileEngineIterator::currentFileInfo() const
{
    m_fileInfo = QFileInfo(currentFilePath());
    return m_fileInfo;
}
//  -----------------------------------------------------------------------

//  A QResourceFileEngineIterator that Python can take functions over in. Every QResourceFileEngineIterator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQResourceFileEngineIteratorCall0)(const void *, int *);
typedef QString * (*CuteQResourceFileEngineIteratorCall1)(const void *, int *);
typedef const QFileInfo * (*CuteQResourceFileEngineIteratorCall2)(const void *, int *);
typedef QString * (*CuteQResourceFileEngineIteratorCall3)(const void *, int *);
class CuteQResourceFileEngineIterator : public QResourceFileEngineIterator {
public:
  using QResourceFileEngineIterator::QResourceFileEngineIterator;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QAbstractFileEngineIterator7advanceEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractFileEngineIterator15currentFileNameEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractFileEngineIterator15currentFileInfoEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractFileEngineIterator15currentFilePathEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool QResourceFileEngineIterator::advance()
  bool advance() override {
    if (taken[0]) {
      int handled = 0;
      CuteQResourceFileEngineIteratorCall0 call = reinterpret_cast<CuteQResourceFileEngineIteratorCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngineIterator::advance();
  }

  //  QString QResourceFileEngineIterator::currentFileName() const
  QString currentFileName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQResourceFileEngineIteratorCall1 call = reinterpret_cast<CuteQResourceFileEngineIteratorCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QResourceFileEngineIterator::currentFileName();
  }

  //  QFileInfo QResourceFileEngineIterator::currentFileInfo() const
  QFileInfo currentFileInfo() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQResourceFileEngineIteratorCall2 call = reinterpret_cast<CuteQResourceFileEngineIteratorCall2>(taken[2]);
      const QFileInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QResourceFileEngineIterator::currentFileInfo();
  }

  //  QString QAbstractFileEngineIterator::currentFilePath() const
  QString currentFilePath() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQResourceFileEngineIteratorCall3 call = reinterpret_cast<CuteQResourceFileEngineIteratorCall3>(taken[3]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAbstractFileEngineIterator::currentFilePath();
  }
};

//  QResourceFileEngineIterator::QResourceFileEngineIterator(const QString
//      &path, QDir::Filters filters, const QStringList &filterNames)
extern "C" Q_DECL_EXPORT
QResourceFileEngineIterator *ritual_ZN27QResourceFileEngineIteratorC1ERK7QString6QFlagsIN4QDir6FilterEERK5QListIS0_E(
    const QString *path,
    int filters,
    const QList<QString> *filterNames) {
  return new CuteQResourceFileEngineIterator(
      *path,
      QFlags<QDir::Filter>::fromInt(filters),
      *filterNames);
}

//  QResourceFileEngineIterator::QResourceFileEngineIterator(const QString
//      &path, QDirListing::IteratorFlags filters, const QStringList
//      &filterNames)
extern "C" Q_DECL_EXPORT
QResourceFileEngineIterator *ritual_ZN27QResourceFileEngineIteratorC1ERK7QString6QFlagsIN11QDirListing12IteratorFlagEERK5QListIS0_E(
    const QString *path,
    int filters,
    const QList<QString> *filterNames) {
  return new CuteQResourceFileEngineIterator(
      *path,
      QFlags<QDirListing::IteratorFlag>::fromInt(filters),
      *filterNames);
}

//  QResourceFileEngineIterator::~QResourceFileEngineIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QResourceFileEngineIteratorD1Ev(
    QResourceFileEngineIterator *self) {
  delete self;
}

//  bool QResourceFileEngineIterator::advance()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QResourceFileEngineIterator7advanceEv(
    QResourceFileEngineIterator *self) {
  return self->advance();
}

//  QString QResourceFileEngineIterator::currentFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QResourceFileEngineIterator15currentFileNameEv(
    const QResourceFileEngineIterator *self) {
  return new QString(self->currentFileName());
}

//  QFileInfo QResourceFileEngineIterator::currentFileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK27QResourceFileEngineIterator15currentFileInfoEv(
    const QResourceFileEngineIterator *self) {
  return new QFileInfo(self->currentFileInfo());
}

//  a Python function taken by a CuteQResourceFileEngineIterator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QResourceFileEngineIterator(
    QResourceFileEngineIterator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQResourceFileEngineIterator *>(self)->take(key, call);
}

//  bool QResourceFileEngineIterator::advance()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QResourceFileEngineIterator7advanceEv(
    QResourceFileEngineIterator *self) {
  return self->QResourceFileEngineIterator::advance();
}

//  QString QResourceFileEngineIterator::currentFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK27QResourceFileEngineIterator15currentFileNameEv(
    const QResourceFileEngineIterator *self) {
  return new QString(self->QResourceFileEngineIterator::currentFileName());
}

//  QFileInfo QResourceFileEngineIterator::currentFileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_own_ZNK27QResourceFileEngineIterator15currentFileInfoEv(
    const QResourceFileEngineIterator *self) {
  return new QFileInfo(self->QResourceFileEngineIterator::currentFileInfo());
}

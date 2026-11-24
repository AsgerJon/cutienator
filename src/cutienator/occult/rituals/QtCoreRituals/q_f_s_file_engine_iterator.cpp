//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfsfileengine_iterator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_FILESYSTEMITERATOR)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfsfileengine_iterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qfileinfo.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qfsfileengine_iterator_p.h>
#include <QtCore/private/qfileinfo_p.h>
#include <QtCore/qvariant.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qfsfileengine_iterator.cpp, line 27, as _ZN21QFSFileEngineIteratorD1Ev
#if !defined(QT_NO_FILESYSTEMITERATOR)
inline QFSFileEngineIterator::~QFSFileEngineIterator()
{
}
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

//  from src/corelib/io/qfsfileengine_iterator.cpp, line 31, as _ZN21QFSFileEngineIterator7advanceEv
#if !defined(QT_NO_FILESYSTEMITERATOR)
inline bool QFSFileEngineIterator::advance()
{
    if (!nativeIterator)
        return false;

    if (auto r = nativeIterator->advance()) {
        m_fileInfo = r->fileInfo();
        return true;
    } else {
        nativeIterator.reset();
        return false;
    }
}
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

//  from src/corelib/io/qfsfileengine_iterator.cpp, line 45, as _ZNK21QFSFileEngineIterator15currentFileNameEv
#if !defined(QT_NO_FILESYSTEMITERATOR)
inline QString QFSFileEngineIterator::currentFileName() const
{
    return m_fileInfo.fileName();
}
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

//  from src/corelib/io/qfsfileengine_iterator.cpp, line 50, as _ZNK21QFSFileEngineIterator15currentFileInfoEv
#if !defined(QT_NO_FILESYSTEMITERATOR)
inline QFileInfo QFSFileEngineIterator::currentFileInfo() const
{
    return m_fileInfo;
}
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)
//  -----------------------------------------------------------------------

//  A QFSFileEngineIterator that Python can take functions over in. Every QFSFileEngineIterator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_FILESYSTEMITERATOR)
typedef bool (*CuteQFSFileEngineIteratorCall0)(const void *, int *);
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)
#if !defined(QT_NO_FILESYSTEMITERATOR)
typedef QString * (*CuteQFSFileEngineIteratorCall1)(const void *, int *);
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)
#if !defined(QT_NO_FILESYSTEMITERATOR)
typedef const QFileInfo * (*CuteQFSFileEngineIteratorCall2)(const void *, int *);
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)
typedef QString * (*CuteQFSFileEngineIteratorCall3)(const void *, int *);
class CuteQFSFileEngineIterator : public QFSFileEngineIterator {
public:
  using QFSFileEngineIterator::QFSFileEngineIterator;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_FILESYSTEMITERATOR)
    if (!std::strcmp(key, "_ZN27QAbstractFileEngineIterator7advanceEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)
#if !defined(QT_NO_FILESYSTEMITERATOR)
    if (!std::strcmp(key, "_ZNK27QAbstractFileEngineIterator15currentFileNameEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)
#if !defined(QT_NO_FILESYSTEMITERATOR)
    if (!std::strcmp(key, "_ZNK27QAbstractFileEngineIterator15currentFileInfoEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)
    if (!std::strcmp(key, "_ZNK27QAbstractFileEngineIterator15currentFilePathEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_FILESYSTEMITERATOR)
  //  bool QFSFileEngineIterator::advance()
  bool advance() override {
    if (taken[0]) {
      int handled = 0;
      CuteQFSFileEngineIteratorCall0 call = reinterpret_cast<CuteQFSFileEngineIteratorCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngineIterator::advance();
  }
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

#if !defined(QT_NO_FILESYSTEMITERATOR)
  //  QString QFSFileEngineIterator::currentFileName() const
  QString currentFileName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFSFileEngineIteratorCall1 call = reinterpret_cast<CuteQFSFileEngineIteratorCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFSFileEngineIterator::currentFileName();
  }
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

#if !defined(QT_NO_FILESYSTEMITERATOR)
  //  QFileInfo QFSFileEngineIterator::currentFileInfo() const
  QFileInfo currentFileInfo() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFSFileEngineIteratorCall2 call = reinterpret_cast<CuteQFSFileEngineIteratorCall2>(taken[2]);
      const QFileInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFSFileEngineIterator::currentFileInfo();
  }
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

  //  QString QAbstractFileEngineIterator::currentFilePath() const
  QString currentFilePath() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFSFileEngineIteratorCall3 call = reinterpret_cast<CuteQFSFileEngineIteratorCall3>(taken[3]);
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

//  QFSFileEngineIterator::~QFSFileEngineIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QFSFileEngineIteratorD1Ev(QFSFileEngineIterator *self) {
  delete self;
}

//  bool QFSFileEngineIterator::advance()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QFSFileEngineIterator7advanceEv(
    QFSFileEngineIterator *self) {
  return self->advance();
}

//  QString QFSFileEngineIterator::currentFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QFSFileEngineIterator15currentFileNameEv(
    const QFSFileEngineIterator *self) {
  return new QString(self->currentFileName());
}

//  QFileInfo QFSFileEngineIterator::currentFileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK21QFSFileEngineIterator15currentFileInfoEv(
    const QFSFileEngineIterator *self) {
  return new QFileInfo(self->currentFileInfo());
}

//  a Python function taken by a CuteQFSFileEngineIterator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFSFileEngineIterator(
    QFSFileEngineIterator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFSFileEngineIterator *>(self)->take(key, call);
}

#if !defined(QT_NO_FILESYSTEMITERATOR)
//  QString QFSFileEngineIterator::currentFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QFSFileEngineIterator15currentFileNameEv(
    const QFSFileEngineIterator *self) {
  return new QString(self->QFSFileEngineIterator::currentFileName());
}
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

#if !defined(QT_NO_FILESYSTEMITERATOR)
//  QFileInfo QFSFileEngineIterator::currentFileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_own_ZNK21QFSFileEngineIterator15currentFileInfoEv(
    const QFSFileEngineIterator *self) {
  return new QFileInfo(self->QFSFileEngineIterator::currentFileInfo());
}
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAbstractFileEngineIterator that Python can take functions over in. Every QAbstractFileEngineIterator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAbstractFileEngineIteratorCall0)(const void *, int *);
typedef QString * (*CuteQAbstractFileEngineIteratorCall1)(const void *, int *);
typedef const QFileInfo * (*CuteQAbstractFileEngineIteratorCall2)(const void *, int *);
typedef QString * (*CuteQAbstractFileEngineIteratorCall3)(const void *, int *);
class CuteQAbstractFileEngineIterator : public QAbstractFileEngineIterator {
public:
  using QAbstractFileEngineIterator::QAbstractFileEngineIterator;
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

  //  bool QAbstractFileEngineIterator::advance()
  bool advance() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractFileEngineIteratorCall0 call = reinterpret_cast<CuteQAbstractFileEngineIteratorCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QAbstractFileEngineIterator::currentFileName() const
  QString currentFileName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractFileEngineIteratorCall1 call = reinterpret_cast<CuteQAbstractFileEngineIteratorCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QFileInfo QAbstractFileEngineIterator::currentFileInfo() const
  QFileInfo currentFileInfo() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractFileEngineIteratorCall2 call = reinterpret_cast<CuteQAbstractFileEngineIteratorCall2>(taken[2]);
      const QFileInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractFileEngineIterator::currentFileInfo();
  }

  //  QString QAbstractFileEngineIterator::currentFilePath() const
  QString currentFilePath() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractFileEngineIteratorCall3 call = reinterpret_cast<CuteQAbstractFileEngineIteratorCall3>(taken[3]);
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

//  QAbstractFileEngineIterator::~QAbstractFileEngineIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractFileEngineIteratorD1Ev(
    QAbstractFileEngineIterator *self) {
  delete self;
}

//  bool QAbstractFileEngineIterator::advance()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QAbstractFileEngineIterator7advanceEv(
    QAbstractFileEngineIterator *self) {
  return self->advance();
}

//  QString QAbstractFileEngineIterator::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QAbstractFileEngineIterator4pathEv(
    const QAbstractFileEngineIterator *self) {
  return new QString(self->path());
}

//  QStringList QAbstractFileEngineIterator::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK27QAbstractFileEngineIterator11nameFiltersEv(
    const QAbstractFileEngineIterator *self) {
  return new QList<QString>(self->nameFilters());
}

//  QDir::Filters QAbstractFileEngineIterator::filters() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QAbstractFileEngineIterator7filtersEv(
    const QAbstractFileEngineIterator *self) {
  return static_cast<int>(self->filters().toInt());
}

//  QString QAbstractFileEngineIterator::currentFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QAbstractFileEngineIterator15currentFileNameEv(
    const QAbstractFileEngineIterator *self) {
  return new QString(self->currentFileName());
}

//  QFileInfo QAbstractFileEngineIterator::currentFileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK27QAbstractFileEngineIterator15currentFileInfoEv(
    const QAbstractFileEngineIterator *self) {
  return new QFileInfo(self->currentFileInfo());
}

//  QString QAbstractFileEngineIterator::currentFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QAbstractFileEngineIterator15currentFilePathEv(
    const QAbstractFileEngineIterator *self) {
  return new QString(self->currentFilePath());
}

//  a Python function taken by a CuteQAbstractFileEngineIterator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractFileEngineIterator(
    QAbstractFileEngineIterator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractFileEngineIterator *>(self)->take(key, call);
}

//  QFileInfo QAbstractFileEngineIterator::currentFileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_own_ZNK27QAbstractFileEngineIterator15currentFileInfoEv(
    const QAbstractFileEngineIterator *self) {
  return new QFileInfo(self->QAbstractFileEngineIterator::currentFileInfo());
}

//  QString QAbstractFileEngineIterator::currentFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK27QAbstractFileEngineIterator15currentFilePathEv(
    const QAbstractFileEngineIterator *self) {
  return new QString(self->QAbstractFileEngineIterator::currentFilePath());
}

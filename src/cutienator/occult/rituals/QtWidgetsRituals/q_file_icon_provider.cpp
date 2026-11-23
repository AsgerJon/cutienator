//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfileiconprovider.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qfileiconprovider.h>
#include <QtGui/qicon.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QFileIconProvider that Python can take functions over in. Every QFileIconProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QIcon * (*CuteQFileIconProviderCall0)(const void *, int, int *);
typedef const QIcon * (*CuteQFileIconProviderCall1)(const void *, const QFileInfo *, int *);
typedef QString * (*CuteQFileIconProviderCall2)(const void *, const QFileInfo *, int *);
typedef void (*CuteQFileIconProviderCall3)(const void *, int, int *);
typedef int (*CuteQFileIconProviderCall4)(const void *, int *);
class CuteQFileIconProvider : public QFileIconProvider {
public:
  using QFileIconProvider::QFileIconProvider;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QAbstractFileIconProvider4iconENS_8IconTypeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAbstractFileIconProvider4iconERK9QFileInfo")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAbstractFileIconProvider4typeERK9QFileInfo")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QAbstractFileIconProvider10setOptionsE6QFlagsINS_6OptionEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAbstractFileIconProvider7optionsEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QIcon QFileIconProvider::icon(IconType type) const
  QIcon icon(QAbstractFileIconProvider::IconType type) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileIconProviderCall0 call = reinterpret_cast<CuteQFileIconProviderCall0>(taken[0]);
      const QIcon * given = call(this, static_cast<int>(type), &handled);
      if (handled && given) return *given;
    }
    return QFileIconProvider::icon(type);
  }

  //  QIcon QFileIconProvider::icon(const QFileInfo &info) const
  QIcon icon(const QFileInfo &info) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileIconProviderCall1 call = reinterpret_cast<CuteQFileIconProviderCall1>(taken[1]);
      const QIcon * given = call(this, &info, &handled);
      if (handled && given) return *given;
    }
    return QFileIconProvider::icon(info);
  }

  //  QString QAbstractFileIconProvider::type(const QFileInfo &a0) const
  QString type(const QFileInfo &a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileIconProviderCall2 call = reinterpret_cast<CuteQFileIconProviderCall2>(taken[2]);
      QString * given = call(this, &a0, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAbstractFileIconProvider::type(a0);
  }

  //  void QAbstractFileIconProvider::setOptions(Options a0)
  void setOptions(QAbstractFileIconProvider::Options a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileIconProviderCall3 call = reinterpret_cast<CuteQFileIconProviderCall3>(taken[3]);
      call(this, static_cast<int>(a0.toInt()), &handled);
      if (handled) return;
    }
    QAbstractFileIconProvider::setOptions(a0);
  }

  //  Options QAbstractFileIconProvider::options() const
  QAbstractFileIconProvider::Options options() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileIconProviderCall4 call = reinterpret_cast<CuteQFileIconProviderCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<QAbstractFileIconProvider::Option>::fromInt(given);
    }
    return QAbstractFileIconProvider::options();
  }
};

//  QFileIconProvider::QFileIconProvider()
extern "C" Q_DECL_EXPORT
QFileIconProvider *ritual_ZN17QFileIconProviderC1Ev() {
  return new CuteQFileIconProvider();
}

//  QFileIconProvider::~QFileIconProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileIconProviderD1Ev(QFileIconProvider *self) {
  delete self;
}

//  QIcon QFileIconProvider::icon(IconType type) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK17QFileIconProvider4iconEN25QAbstractFileIconProvider8IconTypeE(
    const QFileIconProvider *self,
    QAbstractFileIconProvider::IconType type) {
  return new QIcon(self->icon(type));
}

//  QIcon QFileIconProvider::icon(const QFileInfo &info) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK17QFileIconProvider4iconERK9QFileInfo(
    const QFileIconProvider *self,
    const QFileInfo *info) {
  return new QIcon(self->icon(*info));
}

//  QFileIconProviderPrivate *QFileIconProvider::d_func()
extern "C" Q_DECL_EXPORT
QFileIconProviderPrivate *ritual_ZN17QFileIconProvider6d_funcEv(
    QFileIconProvider *self) {
  return self->d_func();
}

//  const QFileIconProviderPrivate *QFileIconProvider::d_func() const
extern "C" Q_DECL_EXPORT
const QFileIconProviderPrivate *ritual_ZNK17QFileIconProvider6d_funcEv(
    const QFileIconProvider *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQFileIconProvider, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileIconProvider(
    QFileIconProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileIconProvider *>(self)->take(key, call);
}

//  QIcon QFileIconProvider::icon(IconType type) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK17QFileIconProvider4iconEN25QAbstractFileIconProvider8IconTypeE(
    const QFileIconProvider *self,
    QAbstractFileIconProvider::IconType type) {
  return new QIcon(self->QFileIconProvider::icon(type));
}

//  QIcon QFileIconProvider::icon(const QFileInfo &info) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK17QFileIconProvider4iconERK9QFileInfo(
    const QFileIconProvider *self,
    const QFileInfo *info) {
  return new QIcon(self->QFileIconProvider::icon(*info));
}

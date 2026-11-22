//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qabstractfileiconprovider.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qabstractfileiconprovider.h>
#include <QtGui/qicon.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAbstractFileIconProvider that Python can take functions over in. Every QAbstractFileIconProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QIcon * (*CuteQAbstractFileIconProviderCall0)(const void *, int, int *);
typedef const QIcon * (*CuteQAbstractFileIconProviderCall1)(const void *, const QFileInfo *, int *);
class CuteQAbstractFileIconProvider : public QAbstractFileIconProvider {
public:
  using QAbstractFileIconProvider::QAbstractFileIconProvider;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QAbstractFileIconProvider4iconENS_8IconTypeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAbstractFileIconProvider4iconERK9QFileInfo")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QIcon QAbstractFileIconProvider::icon(IconType a0) const
  QIcon icon(QAbstractFileIconProvider::IconType a0) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractFileIconProviderCall0 call = reinterpret_cast<CuteQAbstractFileIconProviderCall0>(taken[0]);
      const QIcon * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QAbstractFileIconProvider::icon(a0);
  }

  //  QIcon QAbstractFileIconProvider::icon(const QFileInfo &a0) const
  QIcon icon(const QFileInfo &a0) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractFileIconProviderCall1 call = reinterpret_cast<CuteQAbstractFileIconProviderCall1>(taken[1]);
      const QIcon * given = call(this, &a0, &handled);
      if (handled && given) return *given;
    }
    return QAbstractFileIconProvider::icon(a0);
  }
};

//  QAbstractFileIconProvider::QAbstractFileIconProvider()
extern "C" Q_DECL_EXPORT
QAbstractFileIconProvider *ritual_ZN25QAbstractFileIconProviderC1Ev() {
  return new CuteQAbstractFileIconProvider();
}

//  QAbstractFileIconProvider::~QAbstractFileIconProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractFileIconProviderD1Ev(
    QAbstractFileIconProvider *self) {
  delete self;
}

//  QIcon QAbstractFileIconProvider::icon(IconType a0) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK25QAbstractFileIconProvider4iconENS_8IconTypeE(
    const QAbstractFileIconProvider *self,
    QAbstractFileIconProvider::IconType a0) {
  return new QIcon(self->icon(a0));
}

//  QIcon QAbstractFileIconProvider::icon(const QFileInfo &a0) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK25QAbstractFileIconProvider4iconERK9QFileInfo(
    const QAbstractFileIconProvider *self,
    const QFileInfo *a0) {
  return new QIcon(self->icon(*a0));
}

//  QString QAbstractFileIconProvider::type(const QFileInfo &a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QAbstractFileIconProvider4typeERK9QFileInfo(
    const QAbstractFileIconProvider *self,
    const QFileInfo *a0) {
  return new QString(self->type(*a0));
}

//  void QAbstractFileIconProvider::setOptions(Options a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractFileIconProvider10setOptionsE6QFlagsINS_6OptionEE(
    QAbstractFileIconProvider *self,
    int a0) {
  self->setOptions(QFlags<QAbstractFileIconProvider::Option>::fromInt(a0));
}

//  Options QAbstractFileIconProvider::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAbstractFileIconProvider7optionsEv(
    const QAbstractFileIconProvider *self) {
  return static_cast<int>(self->options().toInt());
}

//  a Python function taken by a CuteQAbstractFileIconProvider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractFileIconProvider(
    QAbstractFileIconProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractFileIconProvider *>(self)->take(key, call);
}

//  QIcon QAbstractFileIconProvider::icon(IconType a0) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK25QAbstractFileIconProvider4iconENS_8IconTypeE(
    const QAbstractFileIconProvider *self,
    QAbstractFileIconProvider::IconType a0) {
  return new QIcon(self->QAbstractFileIconProvider::icon(a0));
}

//  QIcon QAbstractFileIconProvider::icon(const QFileInfo &a0) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_own_ZNK25QAbstractFileIconProvider4iconERK9QFileInfo(
    const QAbstractFileIconProvider *self,
    const QFileInfo *a0) {
  return new QIcon(self->QAbstractFileIconProvider::icon(*a0));
}

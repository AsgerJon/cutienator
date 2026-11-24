//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlGuiProvider that Python can take functions over in. Every QQmlGuiProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQmlGuiProviderCall0)(const void *, QObject *, int *);
typedef void * (*CuteQQmlGuiProviderCall1)(const void *, int *);
typedef void * (*CuteQQmlGuiProviderCall2)(const void *, int *);
typedef bool (*CuteQQmlGuiProviderCall3)(const void *, const QUrl *, int *);
typedef QString * (*CuteQQmlGuiProviderCall4)(const void *, int *);
class CuteQQmlGuiProvider : public QQmlGuiProvider {
public:
  using QQmlGuiProvider::QQmlGuiProvider;
  CuteQQmlGuiProvider(const QQmlGuiProvider &other) : QQmlGuiProvider(other) {}
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QQmlGuiProvider11applicationEP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQmlGuiProvider11inputMethodEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQmlGuiProvider10styleHintsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQmlGuiProvider17openUrlExternallyERK4QUrl")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QQmlGuiProvider10pluginNameEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QQmlApplication *QQmlGuiProvider::application(QObject *parent)
  QQmlApplication *application(QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlGuiProviderCall0 call = reinterpret_cast<CuteQQmlGuiProviderCall0>(taken[0]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QQmlApplication *>(given);
    }
    return QQmlGuiProvider::application(parent);
  }

  //  QObject *QQmlGuiProvider::inputMethod()
  QObject *inputMethod() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlGuiProviderCall1 call = reinterpret_cast<CuteQQmlGuiProviderCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlGuiProvider::inputMethod();
  }

  //  QObject *QQmlGuiProvider::styleHints()
  QObject *styleHints() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlGuiProviderCall2 call = reinterpret_cast<CuteQQmlGuiProviderCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlGuiProvider::styleHints();
  }

  //  bool QQmlGuiProvider::openUrlExternally(const QUrl &a0)
  bool openUrlExternally(const QUrl &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlGuiProviderCall3 call = reinterpret_cast<CuteQQmlGuiProviderCall3>(taken[3]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQmlGuiProvider::openUrlExternally(a0);
  }

  //  QString QQmlGuiProvider::pluginName() const
  QString pluginName() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlGuiProviderCall4 call = reinterpret_cast<CuteQQmlGuiProviderCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlGuiProvider::pluginName();
  }
};

//  QQmlGuiProvider::~QQmlGuiProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlGuiProviderD1Ev(QQmlGuiProvider *self) {
  delete self;
}

//  QQmlApplication *QQmlGuiProvider::application(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlApplication *ritual_ZN15QQmlGuiProvider11applicationEP7QObject(
    QQmlGuiProvider *self,
    QObject *parent) {
  return self->application(parent);
}

//  QObject *QQmlGuiProvider::inputMethod()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN15QQmlGuiProvider11inputMethodEv(QQmlGuiProvider *self) {
  return self->inputMethod();
}

//  QObject *QQmlGuiProvider::styleHints()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN15QQmlGuiProvider10styleHintsEv(QQmlGuiProvider *self) {
  return self->styleHints();
}

//  QStringList QQmlGuiProvider::fontFamilies()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN15QQmlGuiProvider12fontFamiliesEv(
    QQmlGuiProvider *self) {
  return new QList<QString>(self->fontFamilies());
}

//  bool QQmlGuiProvider::openUrlExternally(const QUrl &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQmlGuiProvider17openUrlExternallyERK4QUrl(
    QQmlGuiProvider *self,
    const QUrl *a0) {
  return self->openUrlExternally(*a0);
}

//  QString QQmlGuiProvider::pluginName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlGuiProvider10pluginNameEv(
    const QQmlGuiProvider *self) {
  return new QString(self->pluginName());
}

//  a Python function taken by a CuteQQmlGuiProvider, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlGuiProvider(
    QQmlGuiProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlGuiProvider *>(self)->take(key, call);
}

//  QQmlApplication *QQmlGuiProvider::application(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlApplication *ritual_own_ZN15QQmlGuiProvider11applicationEP7QObject(
    QQmlGuiProvider *self,
    QObject *parent) {
  return self->QQmlGuiProvider::application(parent);
}

//  QObject *QQmlGuiProvider::inputMethod()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN15QQmlGuiProvider11inputMethodEv(
    QQmlGuiProvider *self) {
  return self->QQmlGuiProvider::inputMethod();
}

//  QObject *QQmlGuiProvider::styleHints()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN15QQmlGuiProvider10styleHintsEv(
    QQmlGuiProvider *self) {
  return self->QQmlGuiProvider::styleHints();
}

//  bool QQmlGuiProvider::openUrlExternally(const QUrl &a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQmlGuiProvider17openUrlExternallyERK4QUrl(
    QQmlGuiProvider *self,
    const QUrl *a0) {
  return self->QQmlGuiProvider::openUrlExternally(*a0);
}

//  QString QQmlGuiProvider::pluginName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QQmlGuiProvider10pluginNameEv(
    const QQmlGuiProvider *self) {
  return new QString(self->QQmlGuiProvider::pluginName());
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/textbuilder_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/textbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>

//  A QTextBuilder that Python can take functions over in. Every QTextBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQTextBuilderCall0)(const void *, const DomProperty *, int *);
typedef const QVariant * (*CuteQTextBuilderCall1)(const void *, const QVariant *, int *);
typedef void * (*CuteQTextBuilderCall2)(const void *, const QVariant *, int *);
class CuteQTextBuilder : public QTextBuilder {
public:
  using QTextBuilder::QTextBuilder;
  CuteQTextBuilder(const QTextBuilder &other) : QTextBuilder(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QTextBuilder8loadTextEPK11DomProperty")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QTextBuilder13toNativeValueERK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QTextBuilder8saveTextERK8QVariant")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QVariant QTextBuilder::loadText(const DomProperty *property) const
  QVariant loadText(const DomProperty *property) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextBuilderCall0 call = reinterpret_cast<CuteQTextBuilderCall0>(taken[0]);
      const QVariant * given = call(this, property, &handled);
      if (handled && given) return *given;
    }
    return QTextBuilder::loadText(property);
  }

  //  QVariant QTextBuilder::toNativeValue(const QVariant &value) const
  QVariant toNativeValue(const QVariant &value) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextBuilderCall1 call = reinterpret_cast<CuteQTextBuilderCall1>(taken[1]);
      const QVariant * given = call(this, &value, &handled);
      if (handled && given) return *given;
    }
    return QTextBuilder::toNativeValue(value);
  }

  //  DomProperty *QTextBuilder::saveText(const QVariant &value) const
  DomProperty *saveText(const QVariant &value) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextBuilderCall2 call = reinterpret_cast<CuteQTextBuilderCall2>(taken[2]);
      void * given = call(this, &value, &handled);
      if (handled) return static_cast<DomProperty *>(given);
    }
    return QTextBuilder::saveText(value);
  }
};

//  QTextBuilder::QTextBuilder()
extern "C" Q_DECL_EXPORT
QTextBuilder *ritual_ZN12QTextBuilderC1Ev() {
  return new CuteQTextBuilder();
}

//  QTextBuilder::~QTextBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextBuilderD1Ev(QTextBuilder *self) {
  delete self;
}

//  QVariant QTextBuilder::loadText(const DomProperty *property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QTextBuilder8loadTextEPK11DomProperty(
    const QTextBuilder *self,
    const DomProperty *property) {
  return new QVariant(self->loadText(property));
}

//  QVariant QTextBuilder::toNativeValue(const QVariant &value) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QTextBuilder13toNativeValueERK8QVariant(
    const QTextBuilder *self,
    const QVariant *value) {
  return new QVariant(self->toNativeValue(*value));
}

//  DomProperty *QTextBuilder::saveText(const QVariant &value) const
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZNK12QTextBuilder8saveTextERK8QVariant(
    const QTextBuilder *self,
    const QVariant *value) {
  return self->saveText(*value);
}

//  a Python function taken by a CuteQTextBuilder, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextBuilder(
    QTextBuilder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextBuilder *>(self)->take(key, call);
}

//  QVariant QTextBuilder::loadText(const DomProperty *property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK12QTextBuilder8loadTextEPK11DomProperty(
    const QTextBuilder *self,
    const DomProperty *property) {
  return new QVariant(self->QTextBuilder::loadText(property));
}

//  QVariant QTextBuilder::toNativeValue(const QVariant &value) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK12QTextBuilder13toNativeValueERK8QVariant(
    const QTextBuilder *self,
    const QVariant *value) {
  return new QVariant(self->QTextBuilder::toNativeValue(*value));
}

//  DomProperty *QTextBuilder::saveText(const QVariant &value) const
extern "C" Q_DECL_EXPORT
DomProperty *ritual_own_ZNK12QTextBuilder8saveTextERK8QVariant(
    const QTextBuilder *self,
    const QVariant *value) {
  return self->QTextBuilder::saveText(*value);
}

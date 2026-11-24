//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <cstring>

//  A QQmlSA::PropertyPass that Python can take functions over in. Every QQmlSA::PropertyPass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlSA_PropertyPassCall0)(const void *, const QQmlSA::Element *, const QString *, const QQmlSA::Binding *, const QQmlSA::Element *, const QQmlSA::Element *, int *);
typedef void (*CuteQQmlSA_PropertyPassCall1)(const void *, const QQmlSA::Element *, const QString *, const QQmlSA::Element *, const QQmlSA::SourceLocation *, int *);
typedef void (*CuteQQmlSA_PropertyPassCall2)(const void *, const QQmlSA::Element *, const QString *, const QQmlSA::Element *, const QQmlSA::SourceLocation *, int *);
typedef void (*CuteQQmlSA_PropertyPassCall3)(const void *, const QQmlSA::Element *, const QString *, const QQmlSA::Element *, const QQmlSA::Element *, const QQmlSA::SourceLocation *, int *);
class CuteQQmlSA_PropertyPass : public QQmlSA::PropertyPass {
public:
  using QQmlSA::PropertyPass::PropertyPass;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlSA12PropertyPass9onBindingERKNS_7ElementERK7QStringRKNS_7BindingES3_S3_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlSA12PropertyPass6onReadERKNS_7ElementERK7QStringS3_NS_14SourceLocationE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlSA12PropertyPass6onCallERKNS_7ElementERK7QStringS3_NS_14SourceLocationE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlSA12PropertyPass7onWriteERKNS_7ElementERK7QStringS3_S3_NS_14SourceLocationE")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QQmlSA::PropertyPass::onBinding(const QQmlSA::Element &element,
  //      const QString &propertyName, const QQmlSA::Binding &binding,
  //      const QQmlSA::Element &bindingScope, const QQmlSA::Element
  //      &value)
  void onBinding(
      const QQmlSA::Element &element,
      const QString &propertyName,
      const QQmlSA::Binding &binding,
      const QQmlSA::Element &bindingScope,
      const QQmlSA::Element &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSA_PropertyPassCall0 call = reinterpret_cast<CuteQQmlSA_PropertyPassCall0>(taken[0]);
      call(this, &element, &propertyName, &binding, &bindingScope, &value, &handled);
      if (handled) return;
    }
    QQmlSA::PropertyPass::onBinding(element, propertyName, binding, bindingScope, value);
  }

  //  void QQmlSA::PropertyPass::onRead(const QQmlSA::Element &element,
  //      const QString &propertyName, const QQmlSA::Element &readScope,
  //      QQmlSA::SourceLocation location)
  void onRead(
      const QQmlSA::Element &element,
      const QString &propertyName,
      const QQmlSA::Element &readScope,
      QQmlSA::SourceLocation location) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSA_PropertyPassCall1 call = reinterpret_cast<CuteQQmlSA_PropertyPassCall1>(taken[1]);
      call(this, &element, &propertyName, &readScope, &location, &handled);
      if (handled) return;
    }
    QQmlSA::PropertyPass::onRead(element, propertyName, readScope, location);
  }

  //  void QQmlSA::PropertyPass::onCall(const QQmlSA::Element &element,
  //      const QString &propertyName, const QQmlSA::Element &readScope,
  //      QQmlSA::SourceLocation location)
  void onCall(
      const QQmlSA::Element &element,
      const QString &propertyName,
      const QQmlSA::Element &readScope,
      QQmlSA::SourceLocation location) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlSA_PropertyPassCall2 call = reinterpret_cast<CuteQQmlSA_PropertyPassCall2>(taken[2]);
      call(this, &element, &propertyName, &readScope, &location, &handled);
      if (handled) return;
    }
    QQmlSA::PropertyPass::onCall(element, propertyName, readScope, location);
  }

  //  void QQmlSA::PropertyPass::onWrite(const QQmlSA::Element &element,
  //      const QString &propertyName, const QQmlSA::Element &value, const
  //      QQmlSA::Element &writeScope, QQmlSA::SourceLocation location)
  void onWrite(
      const QQmlSA::Element &element,
      const QString &propertyName,
      const QQmlSA::Element &value,
      const QQmlSA::Element &writeScope,
      QQmlSA::SourceLocation location) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlSA_PropertyPassCall3 call = reinterpret_cast<CuteQQmlSA_PropertyPassCall3>(taken[3]);
      call(this, &element, &propertyName, &value, &writeScope, &location, &handled);
      if (handled) return;
    }
    QQmlSA::PropertyPass::onWrite(element, propertyName, value, writeScope, location);
  }
};

//  void QQmlSA::PropertyPass::onBinding(const QQmlSA::Element &element,
//      const QString &propertyName, const QQmlSA::Binding &binding, const
//      QQmlSA::Element &bindingScope, const QQmlSA::Element &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA12PropertyPass9onBindingERKNS_7ElementERK7QStringRKNS_7BindingES3_S3_(
    QQmlSA::PropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Binding *binding,
    const QQmlSA::Element *bindingScope,
    const QQmlSA::Element *value) {
  self->onBinding(*element, *propertyName, *binding, *bindingScope, *value);
}

//  void QQmlSA::PropertyPass::onRead(const QQmlSA::Element &element, const
//      QString &propertyName, const QQmlSA::Element &readScope,
//      QQmlSA::SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA12PropertyPass6onReadERKNS_7ElementERK7QStringS3_NS_14SourceLocationE(
    QQmlSA::PropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->onRead(*element, *propertyName, *readScope, *location);
}

//  void QQmlSA::PropertyPass::onCall(const QQmlSA::Element &element, const
//      QString &propertyName, const QQmlSA::Element &readScope,
//      QQmlSA::SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA12PropertyPass6onCallERKNS_7ElementERK7QStringS3_NS_14SourceLocationE(
    QQmlSA::PropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->onCall(*element, *propertyName, *readScope, *location);
}

//  void QQmlSA::PropertyPass::onWrite(const QQmlSA::Element &element, const
//      QString &propertyName, const QQmlSA::Element &value, const
//      QQmlSA::Element &writeScope, QQmlSA::SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA12PropertyPass7onWriteERKNS_7ElementERK7QStringS3_S3_NS_14SourceLocationE(
    QQmlSA::PropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *value,
    const QQmlSA::Element *writeScope,
    const QQmlSA::SourceLocation *location) {
  self->onWrite(*element, *propertyName, *value, *writeScope, *location);
}

//  a Python function taken by a CuteQQmlSA_PropertyPass, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSA_PropertyPass(
    QQmlSA::PropertyPass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSA_PropertyPass *>(self)->take(key, call);
}

//  void QQmlSA::PropertyPass::onBinding(const QQmlSA::Element &element,
//      const QString &propertyName, const QQmlSA::Binding &binding, const
//      QQmlSA::Element &bindingScope, const QQmlSA::Element &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlSA12PropertyPass9onBindingERKNS_7ElementERK7QStringRKNS_7BindingES3_S3_(
    QQmlSA::PropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Binding *binding,
    const QQmlSA::Element *bindingScope,
    const QQmlSA::Element *value) {
  self->QQmlSA::PropertyPass::onBinding(
      *element,
      *propertyName,
      *binding,
      *bindingScope,
      *value);
}

//  void QQmlSA::PropertyPass::onRead(const QQmlSA::Element &element, const
//      QString &propertyName, const QQmlSA::Element &readScope,
//      QQmlSA::SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlSA12PropertyPass6onReadERKNS_7ElementERK7QStringS3_NS_14SourceLocationE(
    QQmlSA::PropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->QQmlSA::PropertyPass::onRead(
      *element,
      *propertyName,
      *readScope,
      *location);
}

//  void QQmlSA::PropertyPass::onCall(const QQmlSA::Element &element, const
//      QString &propertyName, const QQmlSA::Element &readScope,
//      QQmlSA::SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlSA12PropertyPass6onCallERKNS_7ElementERK7QStringS3_NS_14SourceLocationE(
    QQmlSA::PropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->QQmlSA::PropertyPass::onCall(
      *element,
      *propertyName,
      *readScope,
      *location);
}

//  void QQmlSA::PropertyPass::onWrite(const QQmlSA::Element &element, const
//      QString &propertyName, const QQmlSA::Element &value, const
//      QQmlSA::Element &writeScope, QQmlSA::SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlSA12PropertyPass7onWriteERKNS_7ElementERK7QStringS3_S3_NS_14SourceLocationE(
    QQmlSA::PropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *value,
    const QQmlSA::Element *writeScope,
    const QQmlSA::SourceLocation *location) {
  self->QQmlSA::PropertyPass::onWrite(
      *element,
      *propertyName,
      *value,
      *writeScope,
      *location);
}

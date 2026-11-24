//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <cstring>

//  A QQmlSA::GenericPropertyPass that Python can take functions over in. Every QQmlSA::GenericPropertyPass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlSA_GenericPropertyPassCall0)(const void *, const QQmlSA::Element *, const QString *, const QQmlSA::Binding *, const QQmlSA::Element *, const QQmlSA::Element *, int *);
typedef void (*CuteQQmlSA_GenericPropertyPassCall1)(const void *, const QQmlSA::Element *, const QString *, const QQmlSA::Element *, const QQmlSA::SourceLocation *, int *);
typedef void (*CuteQQmlSA_GenericPropertyPassCall2)(const void *, const QQmlSA::Element *, const QString *, const QQmlSA::Element *, const QQmlSA::SourceLocation *, int *);
typedef void (*CuteQQmlSA_GenericPropertyPassCall3)(const void *, const QQmlSA::Element *, const QString *, const QQmlSA::Element *, const QQmlSA::Element *, const QQmlSA::SourceLocation *, int *);
class CuteQQmlSA_GenericPropertyPass : public QQmlSA::GenericPropertyPass {
public:
  using QQmlSA::GenericPropertyPass::GenericPropertyPass;
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

  //  void QQmlSA::GenericPropertyPass::onBinding(const Element &element,
  //      const QString &propertyName, const Binding &binding, const
  //      Element &bindingScope, const Element &value)
  void onBinding(
      const QQmlSA::Element &element,
      const QString &propertyName,
      const QQmlSA::Binding &binding,
      const QQmlSA::Element &bindingScope,
      const QQmlSA::Element &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSA_GenericPropertyPassCall0 call = reinterpret_cast<CuteQQmlSA_GenericPropertyPassCall0>(taken[0]);
      call(this, &element, &propertyName, &binding, &bindingScope, &value, &handled);
      if (handled) return;
    }
    QQmlSA::GenericPropertyPass::onBinding(element, propertyName, binding, bindingScope, value);
  }

  //  void QQmlSA::GenericPropertyPass::onRead(const Element &element,
  //      const QString &propertyName, const Element &readScope,
  //      SourceLocation location)
  void onRead(
      const QQmlSA::Element &element,
      const QString &propertyName,
      const QQmlSA::Element &readScope,
      QQmlSA::SourceLocation location) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSA_GenericPropertyPassCall1 call = reinterpret_cast<CuteQQmlSA_GenericPropertyPassCall1>(taken[1]);
      call(this, &element, &propertyName, &readScope, &location, &handled);
      if (handled) return;
    }
    QQmlSA::GenericPropertyPass::onRead(element, propertyName, readScope, location);
  }

  //  void QQmlSA::GenericPropertyPass::onCall(const Element &element,
  //      const QString &propertyName, const Element &readScope,
  //      SourceLocation location)
  void onCall(
      const QQmlSA::Element &element,
      const QString &propertyName,
      const QQmlSA::Element &readScope,
      QQmlSA::SourceLocation location) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlSA_GenericPropertyPassCall2 call = reinterpret_cast<CuteQQmlSA_GenericPropertyPassCall2>(taken[2]);
      call(this, &element, &propertyName, &readScope, &location, &handled);
      if (handled) return;
    }
    QQmlSA::GenericPropertyPass::onCall(element, propertyName, readScope, location);
  }

  //  void QQmlSA::GenericPropertyPass::onWrite(const Element &element,
  //      const QString &propertyName, const Element &value, const Element
  //      &writeScope, SourceLocation location)
  void onWrite(
      const QQmlSA::Element &element,
      const QString &propertyName,
      const QQmlSA::Element &value,
      const QQmlSA::Element &writeScope,
      QQmlSA::SourceLocation location) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlSA_GenericPropertyPassCall3 call = reinterpret_cast<CuteQQmlSA_GenericPropertyPassCall3>(taken[3]);
      call(this, &element, &propertyName, &value, &writeScope, &location, &handled);
      if (handled) return;
    }
    QQmlSA::GenericPropertyPass::onWrite(element, propertyName, value, writeScope, location);
  }
};

//  void QQmlSA::GenericPropertyPass::onBindingDefault(PropertyPass *a0,
//      const Element &a1, const QString &a2, const Binding &a3, const
//      Element &a4, const Element &a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19GenericPropertyPass16onBindingDefaultEPNS_12PropertyPassERKNS_7ElementERK7QStringRKNS_7BindingES5_S5_(
    QQmlSA::PropertyPass *a0,
    const QQmlSA::Element *a1,
    const QString *a2,
    const QQmlSA::Binding *a3,
    const QQmlSA::Element *a4,
    const QQmlSA::Element *a5) {
  QQmlSA::GenericPropertyPass::onBindingDefault(a0, *a1, *a2, *a3, *a4, *a5);
}

//  void QQmlSA::GenericPropertyPass::onReadDefault(PropertyPass *a0, const
//      Element &a1, const QString &a2, const Element &a3, SourceLocation a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19GenericPropertyPass13onReadDefaultEPNS_12PropertyPassERKNS_7ElementERK7QStringS5_NS_14SourceLocationE(
    QQmlSA::PropertyPass *a0,
    const QQmlSA::Element *a1,
    const QString *a2,
    const QQmlSA::Element *a3,
    const QQmlSA::SourceLocation *a4) {
  QQmlSA::GenericPropertyPass::onReadDefault(a0, *a1, *a2, *a3, *a4);
}

//  void QQmlSA::GenericPropertyPass::onCallDefault(PropertyPass *a0, const
//      Element &a1, const QString &a2, const Element &a3, SourceLocation a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19GenericPropertyPass13onCallDefaultEPNS_12PropertyPassERKNS_7ElementERK7QStringS5_NS_14SourceLocationE(
    QQmlSA::PropertyPass *a0,
    const QQmlSA::Element *a1,
    const QString *a2,
    const QQmlSA::Element *a3,
    const QQmlSA::SourceLocation *a4) {
  QQmlSA::GenericPropertyPass::onCallDefault(a0, *a1, *a2, *a3, *a4);
}

//  void QQmlSA::GenericPropertyPass::onWriteDefault(PropertyPass *a0, const
//      Element &a1, const QString &a2, const Element &a3, const Element &a4,
//      SourceLocation a5)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19GenericPropertyPass14onWriteDefaultEPNS_12PropertyPassERKNS_7ElementERK7QStringS5_S5_NS_14SourceLocationE(
    QQmlSA::PropertyPass *a0,
    const QQmlSA::Element *a1,
    const QString *a2,
    const QQmlSA::Element *a3,
    const QQmlSA::Element *a4,
    const QQmlSA::SourceLocation *a5) {
  QQmlSA::GenericPropertyPass::onWriteDefault(a0, *a1, *a2, *a3, *a4, *a5);
}

//  void QQmlSA::GenericPropertyPass::onBinding(const Element &element, const
//      QString &propertyName, const Binding &binding, const Element
//      &bindingScope, const Element &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19GenericPropertyPass9onBindingERKNS_7ElementERK7QStringRKNS_7BindingES3_S3_(
    QQmlSA::GenericPropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Binding *binding,
    const QQmlSA::Element *bindingScope,
    const QQmlSA::Element *value) {
  self->onBinding(*element, *propertyName, *binding, *bindingScope, *value);
}

//  void QQmlSA::GenericPropertyPass::onRead(const Element &element, const
//      QString &propertyName, const Element &readScope, SourceLocation
//      location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19GenericPropertyPass6onReadERKNS_7ElementERK7QStringS3_NS_14SourceLocationE(
    QQmlSA::GenericPropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->onRead(*element, *propertyName, *readScope, *location);
}

//  void QQmlSA::GenericPropertyPass::onCall(const Element &element, const
//      QString &propertyName, const Element &readScope, SourceLocation
//      location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19GenericPropertyPass6onCallERKNS_7ElementERK7QStringS3_NS_14SourceLocationE(
    QQmlSA::GenericPropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->onCall(*element, *propertyName, *readScope, *location);
}

//  void QQmlSA::GenericPropertyPass::onWrite(const Element &element, const
//      QString &propertyName, const Element &value, const Element
//      &writeScope, SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA19GenericPropertyPass7onWriteERKNS_7ElementERK7QStringS3_S3_NS_14SourceLocationE(
    QQmlSA::GenericPropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *value,
    const QQmlSA::Element *writeScope,
    const QQmlSA::SourceLocation *location) {
  self->onWrite(*element, *propertyName, *value, *writeScope, *location);
}

//  a Python function taken by a CuteQQmlSA_GenericPropertyPass, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSA_GenericPropertyPass(
    QQmlSA::GenericPropertyPass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSA_GenericPropertyPass *>(self)->take(key, call);
}

//  void QQmlSA::GenericPropertyPass::onBinding(const Element &element, const
//      QString &propertyName, const Binding &binding, const Element
//      &bindingScope, const Element &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlSA19GenericPropertyPass9onBindingERKNS_7ElementERK7QStringRKNS_7BindingES3_S3_(
    QQmlSA::GenericPropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Binding *binding,
    const QQmlSA::Element *bindingScope,
    const QQmlSA::Element *value) {
  self->QQmlSA::GenericPropertyPass::onBinding(
      *element,
      *propertyName,
      *binding,
      *bindingScope,
      *value);
}

//  void QQmlSA::GenericPropertyPass::onRead(const Element &element, const
//      QString &propertyName, const Element &readScope, SourceLocation
//      location)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlSA19GenericPropertyPass6onReadERKNS_7ElementERK7QStringS3_NS_14SourceLocationE(
    QQmlSA::GenericPropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->QQmlSA::GenericPropertyPass::onRead(
      *element,
      *propertyName,
      *readScope,
      *location);
}

//  void QQmlSA::GenericPropertyPass::onCall(const Element &element, const
//      QString &propertyName, const Element &readScope, SourceLocation
//      location)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlSA19GenericPropertyPass6onCallERKNS_7ElementERK7QStringS3_NS_14SourceLocationE(
    QQmlSA::GenericPropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *readScope,
    const QQmlSA::SourceLocation *location) {
  self->QQmlSA::GenericPropertyPass::onCall(
      *element,
      *propertyName,
      *readScope,
      *location);
}

//  void QQmlSA::GenericPropertyPass::onWrite(const Element &element, const
//      QString &propertyName, const Element &value, const Element
//      &writeScope, SourceLocation location)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlSA19GenericPropertyPass7onWriteERKNS_7ElementERK7QStringS3_S3_NS_14SourceLocationE(
    QQmlSA::GenericPropertyPass *self,
    const QQmlSA::Element *element,
    const QString *propertyName,
    const QQmlSA::Element *value,
    const QQmlSA::Element *writeScope,
    const QQmlSA::SourceLocation *location) {
  self->QQmlSA::GenericPropertyPass::onWrite(
      *element,
      *propertyName,
      *value,
      *writeScope,
      *location);
}

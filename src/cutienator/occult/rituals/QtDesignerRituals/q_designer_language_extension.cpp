//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractlanguage.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractlanguage.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QDesignerLanguageExtension that Python can take functions over in. Every QDesignerLanguageExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQDesignerLanguageExtensionCall0)(const void *, int *);
typedef void * (*CuteQDesignerLanguageExtensionCall1)(const void *, QDesignerFormWindowInterface *, QWidget *, int *);
typedef void * (*CuteQDesignerLanguageExtensionCall2)(const void *, QWidget *, int *);
typedef void * (*CuteQDesignerLanguageExtensionCall3)(const void *, QDesignerFormEditorInterface *, QWidget *, int *);
typedef void * (*CuteQDesignerLanguageExtensionCall4)(const void *, QDesignerFormEditorInterface *, const QString *, QString *, QWidget *, int *);
typedef bool (*CuteQDesignerLanguageExtensionCall5)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerLanguageExtensionCall6)(const void *, QObject *, int *);
typedef bool (*CuteQDesignerLanguageExtensionCall7)(const void *, const QString *, const QString *, int *);
typedef QString * (*CuteQDesignerLanguageExtensionCall8)(const void *, int *);
typedef QString * (*CuteQDesignerLanguageExtensionCall9)(const void *, int *);
class CuteQDesignerLanguageExtension : public QDesignerLanguageExtension {
public:
  using QDesignerLanguageExtension::QDesignerLanguageExtension;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QDesignerLanguageExtension4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDesignerLanguageExtension30createFormWindowSettingsDialogEP28QDesignerFormWindowInterfaceP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDesignerLanguageExtension21createResourceBrowserEP7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDesignerLanguageExtension21createPromotionDialogEP28QDesignerFormEditorInterfaceP7QWidget")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDesignerLanguageExtension21createPromotionDialogEP28QDesignerFormEditorInterfaceRK7QStringPS2_P7QWidget")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerLanguageExtension18isLanguageResourceERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerLanguageExtension11classNameOfEP7QObject")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerLanguageExtension17signalMatchesSlotERK7QStringS2_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerLanguageExtension17widgetBoxContentsEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerLanguageExtension11uiExtensionEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  QString QDesignerLanguageExtension::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall0 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QDialog *QDesignerLanguageExtension::createFormWindowSettingsDialog(Q
  //      DesignerFormWindowInterface *formWindow, QWidget *parentWidget)
  QDialog *createFormWindowSettingsDialog(
      QDesignerFormWindowInterface *formWindow,
      QWidget *parentWidget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall1 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall1>(taken[1]);
      void * given = call(this, formWindow, parentWidget, &handled);
      if (handled) return static_cast<QDialog *>(given);
    }
    return {};
  }

  //  QDesignerResourceBrowserInterface
  //      *QDesignerLanguageExtension::createResourceBrowser(QWidget
  //      *parentWidget)
  QDesignerResourceBrowserInterface *createResourceBrowser(
      QWidget *parentWidget) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall2 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall2>(taken[2]);
      void * given = call(this, parentWidget, &handled);
      if (handled) return static_cast<QDesignerResourceBrowserInterface *>(given);
    }
    return {};
  }

  //  QDialog *QDesignerLanguageExtension::createPromotionDialog(QDesignerF
  //      ormEditorInterface *formEditor, QWidget *parentWidget)
  QDialog *createPromotionDialog(
      QDesignerFormEditorInterface *formEditor,
      QWidget *parentWidget) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall3 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall3>(taken[3]);
      void * given = call(this, formEditor, parentWidget, &handled);
      if (handled) return static_cast<QDialog *>(given);
    }
    return {};
  }

  //  QDialog *QDesignerLanguageExtension::createPromotionDialog(QDesignerF
  //      ormEditorInterface *formEditor, const QString
  //      &promotableWidgetClassName, QString *promoteToClassName, QWidget
  //      *parentWidget)
  QDialog *createPromotionDialog(
      QDesignerFormEditorInterface *formEditor,
      const QString &promotableWidgetClassName,
      QString *promoteToClassName,
      QWidget *parentWidget) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall4 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall4>(taken[4]);
      void * given = call(this, formEditor, &promotableWidgetClassName, promoteToClassName, parentWidget, &handled);
      if (handled) return static_cast<QDialog *>(given);
    }
    return {};
  }

  //  bool QDesignerLanguageExtension::isLanguageResource(const QString
  //      &path) const
  bool isLanguageResource(const QString &path) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall5 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall5>(taken[5]);
      bool given = call(this, &path, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerLanguageExtension::classNameOf(QObject *object)
  //      const
  QString classNameOf(QObject *object) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall6 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall6>(taken[6]);
      QString * given = call(this, object, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  bool QDesignerLanguageExtension::signalMatchesSlot(const QString
  //      &signal, const QString &slot) const
  bool signalMatchesSlot(
      const QString &signal,
      const QString &slot) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall7 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall7>(taken[7]);
      bool given = call(this, &signal, &slot, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerLanguageExtension::widgetBoxContents() const
  QString widgetBoxContents() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall8 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerLanguageExtension::uiExtension() const
  QString uiExtension() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerLanguageExtensionCall9 call = reinterpret_cast<CuteQDesignerLanguageExtensionCall9>(taken[9]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QDesignerLanguageExtension::~QDesignerLanguageExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDesignerLanguageExtensionD1Ev(
    QDesignerLanguageExtension *self) {
  delete self;
}

//  QString QDesignerLanguageExtension::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerLanguageExtension4nameEv(
    const QDesignerLanguageExtension *self) {
  return new QString(self->name());
}

//  QDialog *QDesignerLanguageExtension::createFormWindowSettingsDialog(QDesi
//      gnerFormWindowInterface *formWindow, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QDialog *ritual_ZN26QDesignerLanguageExtension30createFormWindowSettingsDialogEP28QDesignerFormWindowInterfaceP7QWidget(
    QDesignerLanguageExtension *self,
    QDesignerFormWindowInterface *formWindow,
    QWidget *parentWidget) {
  return self->createFormWindowSettingsDialog(formWindow, parentWidget);
}

//  QDesignerResourceBrowserInterface
//      *QDesignerLanguageExtension::createResourceBrowser(QWidget
//      *parentWidget)
extern "C" Q_DECL_EXPORT
QDesignerResourceBrowserInterface *ritual_ZN26QDesignerLanguageExtension21createResourceBrowserEP7QWidget(
    QDesignerLanguageExtension *self,
    QWidget *parentWidget) {
  return self->createResourceBrowser(parentWidget);
}

//  QDialog *QDesignerLanguageExtension::createPromotionDialog(QDesignerFormE
//      ditorInterface *formEditor, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QDialog *ritual_ZN26QDesignerLanguageExtension21createPromotionDialogEP28QDesignerFormEditorInterfaceP7QWidget(
    QDesignerLanguageExtension *self,
    QDesignerFormEditorInterface *formEditor,
    QWidget *parentWidget) {
  return self->createPromotionDialog(formEditor, parentWidget);
}

//  QDialog *QDesignerLanguageExtension::createPromotionDialog(QDesignerFormE
//      ditorInterface *formEditor, const QString &promotableWidgetClassName,
//      QString *promoteToClassName, QWidget *parentWidget)
extern "C" Q_DECL_EXPORT
QDialog *ritual_ZN26QDesignerLanguageExtension21createPromotionDialogEP28QDesignerFormEditorInterfaceRK7QStringPS2_P7QWidget(
    QDesignerLanguageExtension *self,
    QDesignerFormEditorInterface *formEditor,
    const QString *promotableWidgetClassName,
    QString *promoteToClassName,
    QWidget *parentWidget) {
  return self->createPromotionDialog(
      formEditor,
      *promotableWidgetClassName,
      promoteToClassName,
      parentWidget);
}

//  bool QDesignerLanguageExtension::isLanguageResource(const QString &path)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDesignerLanguageExtension18isLanguageResourceERK7QString(
    const QDesignerLanguageExtension *self,
    const QString *path) {
  return self->isLanguageResource(*path);
}

//  QString QDesignerLanguageExtension::classNameOf(QObject *object) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerLanguageExtension11classNameOfEP7QObject(
    const QDesignerLanguageExtension *self,
    QObject *object) {
  return new QString(self->classNameOf(object));
}

//  bool QDesignerLanguageExtension::signalMatchesSlot(const QString &signal,
//      const QString &slot) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDesignerLanguageExtension17signalMatchesSlotERK7QStringS2_(
    const QDesignerLanguageExtension *self,
    const QString *signal,
    const QString *slot) {
  return self->signalMatchesSlot(*signal, *slot);
}

//  QString QDesignerLanguageExtension::widgetBoxContents() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerLanguageExtension17widgetBoxContentsEv(
    const QDesignerLanguageExtension *self) {
  return new QString(self->widgetBoxContents());
}

//  QString QDesignerLanguageExtension::uiExtension() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerLanguageExtension11uiExtensionEv(
    const QDesignerLanguageExtension *self) {
  return new QString(self->uiExtension());
}

//  a Python function taken by a CuteQDesignerLanguageExtension, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerLanguageExtension(
    QDesignerLanguageExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerLanguageExtension *>(self)->take(key, call);
}

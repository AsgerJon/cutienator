//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/extrainfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/extrainfo.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QDesignerExtraInfoExtension that Python can take functions over in. Every QDesignerExtraInfoExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerExtraInfoExtensionCall0)(const void *, int *);
typedef void * (*CuteQDesignerExtraInfoExtensionCall1)(const void *, int *);
typedef bool (*CuteQDesignerExtraInfoExtensionCall2)(const void *, DomUI *, int *);
typedef bool (*CuteQDesignerExtraInfoExtensionCall3)(const void *, DomUI *, int *);
typedef bool (*CuteQDesignerExtraInfoExtensionCall4)(const void *, DomWidget *, int *);
typedef bool (*CuteQDesignerExtraInfoExtensionCall5)(const void *, DomWidget *, int *);
class CuteQDesignerExtraInfoExtension : public QDesignerExtraInfoExtension {
public:
  using QDesignerExtraInfoExtension::QDesignerExtraInfoExtension;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK27QDesignerExtraInfoExtension4coreEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QDesignerExtraInfoExtension6widgetEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerExtraInfoExtension15saveUiExtraInfoEP5DomUI")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerExtraInfoExtension15loadUiExtraInfoEP5DomUI")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerExtraInfoExtension19saveWidgetExtraInfoEP9DomWidget")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDesignerExtraInfoExtension19loadWidgetExtraInfoEP9DomWidget")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  QDesignerFormEditorInterface *QDesignerExtraInfoExtension::core()
  //      const
  QDesignerFormEditorInterface *core() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerExtraInfoExtensionCall0 call = reinterpret_cast<CuteQDesignerExtraInfoExtensionCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return {};
  }

  //  QWidget *QDesignerExtraInfoExtension::widget() const
  QWidget *widget() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerExtraInfoExtensionCall1 call = reinterpret_cast<CuteQDesignerExtraInfoExtensionCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  bool QDesignerExtraInfoExtension::saveUiExtraInfo(DomUI *ui)
  bool saveUiExtraInfo(DomUI *ui) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerExtraInfoExtensionCall2 call = reinterpret_cast<CuteQDesignerExtraInfoExtensionCall2>(taken[2]);
      bool given = call(this, ui, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerExtraInfoExtension::loadUiExtraInfo(DomUI *ui)
  bool loadUiExtraInfo(DomUI *ui) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerExtraInfoExtensionCall3 call = reinterpret_cast<CuteQDesignerExtraInfoExtensionCall3>(taken[3]);
      bool given = call(this, ui, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerExtraInfoExtension::saveWidgetExtraInfo(DomWidget
  //      *ui_widget)
  bool saveWidgetExtraInfo(DomWidget *ui_widget) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerExtraInfoExtensionCall4 call = reinterpret_cast<CuteQDesignerExtraInfoExtensionCall4>(taken[4]);
      bool given = call(this, ui_widget, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerExtraInfoExtension::loadWidgetExtraInfo(DomWidget
  //      *ui_widget)
  bool loadWidgetExtraInfo(DomWidget *ui_widget) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerExtraInfoExtensionCall5 call = reinterpret_cast<CuteQDesignerExtraInfoExtensionCall5>(taken[5]);
      bool given = call(this, ui_widget, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDesignerExtraInfoExtension::QDesignerExtraInfoExtension()
extern "C" Q_DECL_EXPORT
QDesignerExtraInfoExtension *ritual_ZN27QDesignerExtraInfoExtensionC1Ev() {
  return new CuteQDesignerExtraInfoExtension();
}

//  QDesignerExtraInfoExtension::~QDesignerExtraInfoExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerExtraInfoExtensionD1Ev(
    QDesignerExtraInfoExtension *self) {
  delete self;
}

//  QDesignerFormEditorInterface *QDesignerExtraInfoExtension::core() const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK27QDesignerExtraInfoExtension4coreEv(
    const QDesignerExtraInfoExtension *self) {
  return self->core();
}

//  QWidget *QDesignerExtraInfoExtension::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK27QDesignerExtraInfoExtension6widgetEv(
    const QDesignerExtraInfoExtension *self) {
  return self->widget();
}

//  bool QDesignerExtraInfoExtension::saveUiExtraInfo(DomUI *ui)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerExtraInfoExtension15saveUiExtraInfoEP5DomUI(
    QDesignerExtraInfoExtension *self,
    DomUI *ui) {
  return self->saveUiExtraInfo(ui);
}

//  bool QDesignerExtraInfoExtension::loadUiExtraInfo(DomUI *ui)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerExtraInfoExtension15loadUiExtraInfoEP5DomUI(
    QDesignerExtraInfoExtension *self,
    DomUI *ui) {
  return self->loadUiExtraInfo(ui);
}

//  bool QDesignerExtraInfoExtension::saveWidgetExtraInfo(DomWidget
//      *ui_widget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerExtraInfoExtension19saveWidgetExtraInfoEP9DomWidget(
    QDesignerExtraInfoExtension *self,
    DomWidget *ui_widget) {
  return self->saveWidgetExtraInfo(ui_widget);
}

//  bool QDesignerExtraInfoExtension::loadWidgetExtraInfo(DomWidget
//      *ui_widget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDesignerExtraInfoExtension19loadWidgetExtraInfoEP9DomWidget(
    QDesignerExtraInfoExtension *self,
    DomWidget *ui_widget) {
  return self->loadWidgetExtraInfo(ui_widget);
}

//  QString QDesignerExtraInfoExtension::workingDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDesignerExtraInfoExtension16workingDirectoryEv(
    const QDesignerExtraInfoExtension *self) {
  return new QString(self->workingDirectory());
}

//  void QDesignerExtraInfoExtension::setWorkingDirectory(const QString
//      &workingDirectory)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDesignerExtraInfoExtension19setWorkingDirectoryERK7QString(
    QDesignerExtraInfoExtension *self,
    const QString *workingDirectory) {
  self->setWorkingDirectory(*workingDirectory);
}

//  a Python function taken by a CuteQDesignerExtraInfoExtension, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerExtraInfoExtension(
    QDesignerExtraInfoExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerExtraInfoExtension *>(self)->take(key, call);
}

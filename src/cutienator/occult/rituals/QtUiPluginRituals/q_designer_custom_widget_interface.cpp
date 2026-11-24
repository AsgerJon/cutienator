//  Written by dev_tooling.RitualGenerator from the records of
//  QtUiPlugin/customwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtUiPlugin/customwidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerCustomWidgetInterface that Python can take functions over in. Every QDesignerCustomWidgetInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQDesignerCustomWidgetInterfaceCall0)(const void *, int *);
typedef QString * (*CuteQDesignerCustomWidgetInterfaceCall1)(const void *, int *);
typedef QString * (*CuteQDesignerCustomWidgetInterfaceCall2)(const void *, int *);
typedef QString * (*CuteQDesignerCustomWidgetInterfaceCall3)(const void *, int *);
typedef QString * (*CuteQDesignerCustomWidgetInterfaceCall4)(const void *, int *);
typedef const QIcon * (*CuteQDesignerCustomWidgetInterfaceCall5)(const void *, int *);
typedef bool (*CuteQDesignerCustomWidgetInterfaceCall6)(const void *, int *);
typedef void * (*CuteQDesignerCustomWidgetInterfaceCall7)(const void *, QWidget *, int *);
typedef bool (*CuteQDesignerCustomWidgetInterfaceCall8)(const void *, int *);
typedef void (*CuteQDesignerCustomWidgetInterfaceCall9)(const void *, QDesignerFormEditorInterface *, int *);
typedef QString * (*CuteQDesignerCustomWidgetInterfaceCall10)(const void *, int *);
typedef QString * (*CuteQDesignerCustomWidgetInterfaceCall11)(const void *, int *);
class CuteQDesignerCustomWidgetInterface : public QDesignerCustomWidgetInterface {
public:
  using QDesignerCustomWidgetInterface::QDesignerCustomWidgetInterface;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface5groupEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface7toolTipEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface9whatsThisEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface11includeFileEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface4iconEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface11isContainerEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerCustomWidgetInterface12createWidgetEP7QWidget")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface13isInitializedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QDesignerCustomWidgetInterface10initializeEP28QDesignerFormEditorInterface")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface6domXmlEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerCustomWidgetInterface12codeTemplateEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  QString QDesignerCustomWidgetInterface::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall0 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerCustomWidgetInterface::group() const
  QString group() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall1 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerCustomWidgetInterface::toolTip() const
  QString toolTip() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall2 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerCustomWidgetInterface::whatsThis() const
  QString whatsThis() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall3 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall3>(taken[3]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerCustomWidgetInterface::includeFile() const
  QString includeFile() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall4 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QIcon QDesignerCustomWidgetInterface::icon() const
  QIcon icon() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall5 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall5>(taken[5]);
      const QIcon * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QDesignerCustomWidgetInterface::isContainer() const
  bool isContainer() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall6 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QWidget *QDesignerCustomWidgetInterface::createWidget(QWidget
  //      *parent)
  QWidget *createWidget(QWidget *parent) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall7 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall7>(taken[7]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  bool QDesignerCustomWidgetInterface::isInitialized() const
  bool isInitialized() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall8 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QDesignerCustomWidgetInterface::isInitialized();
  }

  //  void QDesignerCustomWidgetInterface::initialize(QDesignerFormEditorIn
  //      terface *core)
  void initialize(QDesignerFormEditorInterface *core) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall9 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall9>(taken[9]);
      call(this, core, &handled);
      if (handled) return;
    }
    QDesignerCustomWidgetInterface::initialize(core);
  }

  //  QString QDesignerCustomWidgetInterface::domXml() const
  QString domXml() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall10 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall10>(taken[10]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerCustomWidgetInterface::domXml();
  }

  //  QString QDesignerCustomWidgetInterface::codeTemplate() const
  QString codeTemplate() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerCustomWidgetInterfaceCall11 call = reinterpret_cast<CuteQDesignerCustomWidgetInterfaceCall11>(taken[11]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerCustomWidgetInterface::codeTemplate();
  }
};

//  QDesignerCustomWidgetInterface::~QDesignerCustomWidgetInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerCustomWidgetInterfaceD1Ev(
    QDesignerCustomWidgetInterface *self) {
  delete self;
}

//  QString QDesignerCustomWidgetInterface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerCustomWidgetInterface4nameEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->name());
}

//  QString QDesignerCustomWidgetInterface::group() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerCustomWidgetInterface5groupEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->group());
}

//  QString QDesignerCustomWidgetInterface::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerCustomWidgetInterface7toolTipEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->toolTip());
}

//  QString QDesignerCustomWidgetInterface::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerCustomWidgetInterface9whatsThisEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->whatsThis());
}

//  QString QDesignerCustomWidgetInterface::includeFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerCustomWidgetInterface11includeFileEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->includeFile());
}

//  QIcon QDesignerCustomWidgetInterface::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK30QDesignerCustomWidgetInterface4iconEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QIcon(self->icon());
}

//  bool QDesignerCustomWidgetInterface::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDesignerCustomWidgetInterface11isContainerEv(
    const QDesignerCustomWidgetInterface *self) {
  return self->isContainer();
}

//  QWidget *QDesignerCustomWidgetInterface::createWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN30QDesignerCustomWidgetInterface12createWidgetEP7QWidget(
    QDesignerCustomWidgetInterface *self,
    QWidget *parent) {
  return self->createWidget(parent);
}

//  bool QDesignerCustomWidgetInterface::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDesignerCustomWidgetInterface13isInitializedEv(
    const QDesignerCustomWidgetInterface *self) {
  return self->isInitialized();
}

//  void
//      QDesignerCustomWidgetInterface::initialize(QDesignerFormEditorInterfa
//      ce *core)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerCustomWidgetInterface10initializeEP28QDesignerFormEditorInterface(
    QDesignerCustomWidgetInterface *self,
    QDesignerFormEditorInterface *core) {
  self->initialize(core);
}

//  QString QDesignerCustomWidgetInterface::domXml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerCustomWidgetInterface6domXmlEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->domXml());
}

//  QString QDesignerCustomWidgetInterface::codeTemplate() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerCustomWidgetInterface12codeTemplateEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->codeTemplate());
}

//  a Python function taken by a CuteQDesignerCustomWidgetInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerCustomWidgetInterface(
    QDesignerCustomWidgetInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerCustomWidgetInterface *>(self)->take(key, call);
}

//  bool QDesignerCustomWidgetInterface::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK30QDesignerCustomWidgetInterface13isInitializedEv(
    const QDesignerCustomWidgetInterface *self) {
  return self->QDesignerCustomWidgetInterface::isInitialized();
}

//  void
//      QDesignerCustomWidgetInterface::initialize(QDesignerFormEditorInterfa
//      ce *core)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QDesignerCustomWidgetInterface10initializeEP28QDesignerFormEditorInterface(
    QDesignerCustomWidgetInterface *self,
    QDesignerFormEditorInterface *core) {
  self->QDesignerCustomWidgetInterface::initialize(core);
}

//  QString QDesignerCustomWidgetInterface::domXml() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK30QDesignerCustomWidgetInterface6domXmlEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->QDesignerCustomWidgetInterface::domXml());
}

//  QString QDesignerCustomWidgetInterface::codeTemplate() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK30QDesignerCustomWidgetInterface12codeTemplateEv(
    const QDesignerCustomWidgetInterface *self) {
  return new QString(self->QDesignerCustomWidgetInterface::codeTemplate());
}

//  QList<QDesignerCustomWidgetInterface *>::QList()
extern "C" Q_DECL_EXPORT
QList<QDesignerCustomWidgetInterface *> *ritual_list_make_QDesignerCustomWidgetInterface_ptr() {
  return new QList<QDesignerCustomWidgetInterface *>();
}

//  void QList<QDesignerCustomWidgetInterface *>::append(const
//      QDesignerCustomWidgetInterface * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDesignerCustomWidgetInterface_ptr(
    QList<QDesignerCustomWidgetInterface *> *self,
    QDesignerCustomWidgetInterface *element) {
  self->append(element);
}

//  qsizetype QList<QDesignerCustomWidgetInterface *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDesignerCustomWidgetInterface_ptr(
    const QList<QDesignerCustomWidgetInterface *> *self) {
  return self->size();
}

//  const QDesignerCustomWidgetInterface *
//      &QList<QDesignerCustomWidgetInterface *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDesignerCustomWidgetInterface *ritual_list_at_QDesignerCustomWidgetInterface_ptr(
    const QList<QDesignerCustomWidgetInterface *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QDesignerCustomWidgetInterface *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDesignerCustomWidgetInterface_ptr(
    QList<QDesignerCustomWidgetInterface *> *self) {
  delete self;
}

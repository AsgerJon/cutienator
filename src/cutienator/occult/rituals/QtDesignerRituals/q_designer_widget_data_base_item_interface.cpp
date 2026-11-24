//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractwidgetdatabase.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDesigner/abstractwidgetdatabase.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerWidgetDataBaseItemInterface that Python can take functions over in. Every QDesignerWidgetDataBaseItemInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQDesignerWidgetDataBaseItemInterfaceCall0)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall1)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerWidgetDataBaseItemInterfaceCall2)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall3)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerWidgetDataBaseItemInterfaceCall4)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall5)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerWidgetDataBaseItemInterfaceCall6)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall7)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerWidgetDataBaseItemInterfaceCall8)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall9)(const void *, const QString *, int *);
typedef const QIcon * (*CuteQDesignerWidgetDataBaseItemInterfaceCall10)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall11)(const void *, const QIcon *, int *);
typedef bool (*CuteQDesignerWidgetDataBaseItemInterfaceCall12)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall13)(const void *, bool, int *);
typedef bool (*CuteQDesignerWidgetDataBaseItemInterfaceCall14)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall15)(const void *, bool, int *);
typedef bool (*CuteQDesignerWidgetDataBaseItemInterfaceCall16)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall17)(const void *, bool, int *);
typedef QString * (*CuteQDesignerWidgetDataBaseItemInterfaceCall18)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall19)(const void *, const QString *, int *);
typedef bool (*CuteQDesignerWidgetDataBaseItemInterfaceCall20)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall21)(const void *, bool, int *);
typedef QString * (*CuteQDesignerWidgetDataBaseItemInterfaceCall22)(const void *, int *);
typedef void (*CuteQDesignerWidgetDataBaseItemInterfaceCall23)(const void *, const QString *, int *);
class CuteQDesignerWidgetDataBaseItemInterface : public QDesignerWidgetDataBaseItemInterface {
public:
  using QDesignerWidgetDataBaseItemInterface::QDesignerWidgetDataBaseItemInterface;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface7setNameERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface5groupEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface8setGroupERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface7toolTipEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface10setToolTipERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface9whatsThisEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface12setWhatsThisERK7QString")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface11includeFileEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface14setIncludeFileERK7QString")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface4iconEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface7setIconERK5QIcon")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface8isCompatEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface9setCompatEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface11isContainerEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface12setContainerEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface8isCustomEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface9setCustomEb")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface10pluginPathEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface13setPluginPathERK7QString")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface10isPromotedEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface11setPromotedEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK36QDesignerWidgetDataBaseItemInterface7extendsEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN36QDesignerWidgetDataBaseItemInterface10setExtendsERK7QString")) {
      taken[23] = call;
      return true;
    }
    return false;
  }

  //  QString QDesignerWidgetDataBaseItemInterface::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall0 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setName(const QString
  //      &name)
  void setName(const QString &name) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall1 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall1>(taken[1]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerWidgetDataBaseItemInterface::group() const
  QString group() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall2 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setGroup(const QString
  //      &group)
  void setGroup(const QString &group) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall3 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall3>(taken[3]);
      call(this, &group, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerWidgetDataBaseItemInterface::toolTip() const
  QString toolTip() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall4 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setToolTip(const QString
  //      &toolTip)
  void setToolTip(const QString &toolTip) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall5 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall5>(taken[5]);
      call(this, &toolTip, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerWidgetDataBaseItemInterface::whatsThis() const
  QString whatsThis() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall6 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setWhatsThis(const QString
  //      &whatsThis)
  void setWhatsThis(const QString &whatsThis) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall7 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall7>(taken[7]);
      call(this, &whatsThis, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerWidgetDataBaseItemInterface::includeFile() const
  QString includeFile() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall8 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setIncludeFile(const
  //      QString &includeFile)
  void setIncludeFile(const QString &includeFile) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall9 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall9>(taken[9]);
      call(this, &includeFile, &handled);
      if (handled) return;
    }
  }

  //  QIcon QDesignerWidgetDataBaseItemInterface::icon() const
  QIcon icon() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall10 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall10>(taken[10]);
      const QIcon * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setIcon(const QIcon &icon)
  void setIcon(const QIcon &icon) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall11 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall11>(taken[11]);
      call(this, &icon, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerWidgetDataBaseItemInterface::isCompat() const
  bool isCompat() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall12 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setCompat(bool compat)
  void setCompat(bool compat) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall13 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall13>(taken[13]);
      call(this, compat, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerWidgetDataBaseItemInterface::isContainer() const
  bool isContainer() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall14 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setContainer(bool
  //      container)
  void setContainer(bool container) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall15 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall15>(taken[15]);
      call(this, container, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerWidgetDataBaseItemInterface::isCustom() const
  bool isCustom() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall16 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setCustom(bool custom)
  void setCustom(bool custom) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall17 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall17>(taken[17]);
      call(this, custom, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerWidgetDataBaseItemInterface::pluginPath() const
  QString pluginPath() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall18 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall18>(taken[18]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setPluginPath(const
  //      QString &path)
  void setPluginPath(const QString &path) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall19 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall19>(taken[19]);
      call(this, &path, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerWidgetDataBaseItemInterface::isPromoted() const
  bool isPromoted() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall20 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setPromoted(bool b)
  void setPromoted(bool b) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall21 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall21>(taken[21]);
      call(this, b, &handled);
      if (handled) return;
    }
  }

  //  QString QDesignerWidgetDataBaseItemInterface::extends() const
  QString extends() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall22 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall22>(taken[22]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerWidgetDataBaseItemInterface::setExtends(const QString
  //      &s)
  void setExtends(const QString &s) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerWidgetDataBaseItemInterfaceCall23 call = reinterpret_cast<CuteQDesignerWidgetDataBaseItemInterfaceCall23>(taken[23]);
      call(this, &s, &handled);
      if (handled) return;
    }
  }
};

//  QDesignerWidgetDataBaseItemInterface::~QDesignerWidgetDataBaseItemInterfa
//      ce()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterfaceD1Ev(
    QDesignerWidgetDataBaseItemInterface *self) {
  delete self;
}

//  QString QDesignerWidgetDataBaseItemInterface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK36QDesignerWidgetDataBaseItemInterface4nameEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QString(self->name());
}

//  void QDesignerWidgetDataBaseItemInterface::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface7setNameERK7QString(
    QDesignerWidgetDataBaseItemInterface *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QDesignerWidgetDataBaseItemInterface::group() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK36QDesignerWidgetDataBaseItemInterface5groupEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QString(self->group());
}

//  void QDesignerWidgetDataBaseItemInterface::setGroup(const QString &group)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface8setGroupERK7QString(
    QDesignerWidgetDataBaseItemInterface *self,
    const QString *group) {
  self->setGroup(*group);
}

//  QString QDesignerWidgetDataBaseItemInterface::toolTip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK36QDesignerWidgetDataBaseItemInterface7toolTipEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QString(self->toolTip());
}

//  void QDesignerWidgetDataBaseItemInterface::setToolTip(const QString
//      &toolTip)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface10setToolTipERK7QString(
    QDesignerWidgetDataBaseItemInterface *self,
    const QString *toolTip) {
  self->setToolTip(*toolTip);
}

//  QString QDesignerWidgetDataBaseItemInterface::whatsThis() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK36QDesignerWidgetDataBaseItemInterface9whatsThisEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QString(self->whatsThis());
}

//  void QDesignerWidgetDataBaseItemInterface::setWhatsThis(const QString
//      &whatsThis)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface12setWhatsThisERK7QString(
    QDesignerWidgetDataBaseItemInterface *self,
    const QString *whatsThis) {
  self->setWhatsThis(*whatsThis);
}

//  QString QDesignerWidgetDataBaseItemInterface::includeFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK36QDesignerWidgetDataBaseItemInterface11includeFileEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QString(self->includeFile());
}

//  void QDesignerWidgetDataBaseItemInterface::setIncludeFile(const QString
//      &includeFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface14setIncludeFileERK7QString(
    QDesignerWidgetDataBaseItemInterface *self,
    const QString *includeFile) {
  self->setIncludeFile(*includeFile);
}

//  QIcon QDesignerWidgetDataBaseItemInterface::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK36QDesignerWidgetDataBaseItemInterface4iconEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QIcon(self->icon());
}

//  void QDesignerWidgetDataBaseItemInterface::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface7setIconERK5QIcon(
    QDesignerWidgetDataBaseItemInterface *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  bool QDesignerWidgetDataBaseItemInterface::isCompat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK36QDesignerWidgetDataBaseItemInterface8isCompatEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return self->isCompat();
}

//  void QDesignerWidgetDataBaseItemInterface::setCompat(bool compat)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface9setCompatEb(
    QDesignerWidgetDataBaseItemInterface *self,
    bool compat) {
  self->setCompat(compat);
}

//  bool QDesignerWidgetDataBaseItemInterface::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK36QDesignerWidgetDataBaseItemInterface11isContainerEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return self->isContainer();
}

//  void QDesignerWidgetDataBaseItemInterface::setContainer(bool container)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface12setContainerEb(
    QDesignerWidgetDataBaseItemInterface *self,
    bool container) {
  self->setContainer(container);
}

//  bool QDesignerWidgetDataBaseItemInterface::isCustom() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK36QDesignerWidgetDataBaseItemInterface8isCustomEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return self->isCustom();
}

//  void QDesignerWidgetDataBaseItemInterface::setCustom(bool custom)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface9setCustomEb(
    QDesignerWidgetDataBaseItemInterface *self,
    bool custom) {
  self->setCustom(custom);
}

//  QString QDesignerWidgetDataBaseItemInterface::pluginPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK36QDesignerWidgetDataBaseItemInterface10pluginPathEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QString(self->pluginPath());
}

//  void QDesignerWidgetDataBaseItemInterface::setPluginPath(const QString
//      &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface13setPluginPathERK7QString(
    QDesignerWidgetDataBaseItemInterface *self,
    const QString *path) {
  self->setPluginPath(*path);
}

//  bool QDesignerWidgetDataBaseItemInterface::isPromoted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK36QDesignerWidgetDataBaseItemInterface10isPromotedEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return self->isPromoted();
}

//  void QDesignerWidgetDataBaseItemInterface::setPromoted(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface11setPromotedEb(
    QDesignerWidgetDataBaseItemInterface *self,
    bool b) {
  self->setPromoted(b);
}

//  QString QDesignerWidgetDataBaseItemInterface::extends() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK36QDesignerWidgetDataBaseItemInterface7extendsEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QString(self->extends());
}

//  void QDesignerWidgetDataBaseItemInterface::setExtends(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface10setExtendsERK7QString(
    QDesignerWidgetDataBaseItemInterface *self,
    const QString *s) {
  self->setExtends(*s);
}

//  void QDesignerWidgetDataBaseItemInterface::setDefaultPropertyValues(const
//      QList<QVariant> &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QDesignerWidgetDataBaseItemInterface24setDefaultPropertyValuesERK5QListI8QVariantE(
    QDesignerWidgetDataBaseItemInterface *self,
    const QList<QVariant> *list) {
  self->setDefaultPropertyValues(*list);
}

//  QList<QVariant>
//      QDesignerWidgetDataBaseItemInterface::defaultPropertyValues() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK36QDesignerWidgetDataBaseItemInterface21defaultPropertyValuesEv(
    const QDesignerWidgetDataBaseItemInterface *self) {
  return new QList<QVariant>(self->defaultPropertyValues());
}

//  a Python function taken by a CuteQDesignerWidgetDataBaseItemInterface,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerWidgetDataBaseItemInterface(
    QDesignerWidgetDataBaseItemInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerWidgetDataBaseItemInterface *>(self)->take(key, call);
}

//  QList<QDesignerWidgetDataBaseItemInterface *>::QList()
extern "C" Q_DECL_EXPORT
QList<QDesignerWidgetDataBaseItemInterface *> *ritual_list_make_QDesignerWidgetDataBaseItemInterface_ptr() {
  return new QList<QDesignerWidgetDataBaseItemInterface *>();
}

//  void QList<QDesignerWidgetDataBaseItemInterface *>::append(const
//      QDesignerWidgetDataBaseItemInterface * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDesignerWidgetDataBaseItemInterface_ptr(
    QList<QDesignerWidgetDataBaseItemInterface *> *self,
    QDesignerWidgetDataBaseItemInterface *element) {
  self->append(element);
}

//  qsizetype QList<QDesignerWidgetDataBaseItemInterface *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDesignerWidgetDataBaseItemInterface_ptr(
    const QList<QDesignerWidgetDataBaseItemInterface *> *self) {
  return self->size();
}

//  const QDesignerWidgetDataBaseItemInterface *
//      &QList<QDesignerWidgetDataBaseItemInterface *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDesignerWidgetDataBaseItemInterface *ritual_list_at_QDesignerWidgetDataBaseItemInterface_ptr(
    const QList<QDesignerWidgetDataBaseItemInterface *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QDesignerWidgetDataBaseItemInterface *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDesignerWidgetDataBaseItemInterface_ptr(
    QList<QDesignerWidgetDataBaseItemInterface *> *self) {
  delete self;
}

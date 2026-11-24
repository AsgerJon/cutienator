//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectsource.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A SourceApiMap that Python can take functions over in. Every SourceApiMap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteSourceApiMapCall0)(const void *, int *);
typedef QString * (*CuteSourceApiMapCall1)(const void *, int *);
typedef const QByteArray * (*CuteSourceApiMapCall2)(const void *, int *);
typedef int (*CuteSourceApiMapCall3)(const void *, int *);
typedef int (*CuteSourceApiMapCall4)(const void *, int *);
typedef int (*CuteSourceApiMapCall5)(const void *, int *);
typedef int (*CuteSourceApiMapCall6)(const void *, int *);
typedef int (*CuteSourceApiMapCall7)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall8)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall9)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall10)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall11)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall12)(const void *, int, int, int *);
typedef const QByteArray * (*CuteSourceApiMapCall13)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall14)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall15)(const void *, int, int, int *);
typedef const QByteArray * (*CuteSourceApiMapCall16)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall17)(const void *, int, int *);
typedef const QByteArray * (*CuteSourceApiMapCall18)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall19)(const void *, int, int *);
typedef int (*CuteSourceApiMapCall20)(const void *, int, int *);
typedef const QByteArray * (*CuteSourceApiMapCall21)(const void *, int *);
typedef bool (*CuteSourceApiMapCall22)(const void *, int *);
typedef bool (*CuteSourceApiMapCall23)(const void *, int, int *);
typedef bool (*CuteSourceApiMapCall24)(const void *, int, int *);
typedef bool (*CuteSourceApiMapCall25)(const void *, int, int *);
class CuteSourceApiMap : public SourceApiMap {
public:
  using SourceApiMap::SourceApiMap;
  void *taken[26] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12SourceApiMap4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap8typeNameEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap9classNameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap9enumCountEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap13propertyCountEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap11signalCountEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap11methodCountEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap15sourceEnumIndexEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap19sourcePropertyIndexEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap17sourceSignalIndexEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap17sourceMethodIndexEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap20signalParameterCountEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap19signalParameterTypeEii")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap15signalSignatureEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap20methodParameterCountEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap19methodParameterTypeEii")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap15methodSignatureEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap10methodTypeEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap8typeNameEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap23propertyIndexFromSignalEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap26propertyRawIndexFromSignalEi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap15objectSignatureEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap9isDynamicEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap15isAdapterSignalEi")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap15isAdapterMethodEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12SourceApiMap17isAdapterPropertyEi")) {
      taken[25] = call;
      return true;
    }
    return false;
  }

  //  QString SourceApiMap::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteSourceApiMapCall0 call = reinterpret_cast<CuteSourceApiMapCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString SourceApiMap::typeName() const
  QString typeName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteSourceApiMapCall1 call = reinterpret_cast<CuteSourceApiMapCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QByteArray SourceApiMap::className() const
  QByteArray className() const override {
    if (taken[2]) {
      int handled = 0;
      CuteSourceApiMapCall2 call = reinterpret_cast<CuteSourceApiMapCall2>(taken[2]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return SourceApiMap::className();
  }

  //  int SourceApiMap::enumCount() const
  int enumCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteSourceApiMapCall3 call = reinterpret_cast<CuteSourceApiMapCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::propertyCount() const
  int propertyCount() const override {
    if (taken[4]) {
      int handled = 0;
      CuteSourceApiMapCall4 call = reinterpret_cast<CuteSourceApiMapCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::signalCount() const
  int signalCount() const override {
    if (taken[5]) {
      int handled = 0;
      CuteSourceApiMapCall5 call = reinterpret_cast<CuteSourceApiMapCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::methodCount() const
  int methodCount() const override {
    if (taken[6]) {
      int handled = 0;
      CuteSourceApiMapCall6 call = reinterpret_cast<CuteSourceApiMapCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::sourceEnumIndex(int index) const
  int sourceEnumIndex(int index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteSourceApiMapCall7 call = reinterpret_cast<CuteSourceApiMapCall7>(taken[7]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::sourcePropertyIndex(int index) const
  int sourcePropertyIndex(int index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteSourceApiMapCall8 call = reinterpret_cast<CuteSourceApiMapCall8>(taken[8]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::sourceSignalIndex(int index) const
  int sourceSignalIndex(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteSourceApiMapCall9 call = reinterpret_cast<CuteSourceApiMapCall9>(taken[9]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::sourceMethodIndex(int index) const
  int sourceMethodIndex(int index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteSourceApiMapCall10 call = reinterpret_cast<CuteSourceApiMapCall10>(taken[10]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::signalParameterCount(int index) const
  int signalParameterCount(int index) const override {
    if (taken[11]) {
      int handled = 0;
      CuteSourceApiMapCall11 call = reinterpret_cast<CuteSourceApiMapCall11>(taken[11]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::signalParameterType(int sigIndex, int paramIndex)
  //      const
  int signalParameterType(int sigIndex, int paramIndex) const override {
    if (taken[12]) {
      int handled = 0;
      CuteSourceApiMapCall12 call = reinterpret_cast<CuteSourceApiMapCall12>(taken[12]);
      int given = call(this, sigIndex, paramIndex, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  const QByteArray SourceApiMap::signalSignature(int index) const
  const QByteArray signalSignature(int index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteSourceApiMapCall13 call = reinterpret_cast<CuteSourceApiMapCall13>(taken[13]);
      const QByteArray * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int SourceApiMap::methodParameterCount(int index) const
  int methodParameterCount(int index) const override {
    if (taken[14]) {
      int handled = 0;
      CuteSourceApiMapCall14 call = reinterpret_cast<CuteSourceApiMapCall14>(taken[14]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::methodParameterType(int methodIndex, int
  //      paramIndex) const
  int methodParameterType(int methodIndex, int paramIndex) const override {
    if (taken[15]) {
      int handled = 0;
      CuteSourceApiMapCall15 call = reinterpret_cast<CuteSourceApiMapCall15>(taken[15]);
      int given = call(this, methodIndex, paramIndex, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  const QByteArray SourceApiMap::methodSignature(int index) const
  const QByteArray methodSignature(int index) const override {
    if (taken[16]) {
      int handled = 0;
      CuteSourceApiMapCall16 call = reinterpret_cast<CuteSourceApiMapCall16>(taken[16]);
      const QByteArray * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QMetaMethod::MethodType SourceApiMap::methodType(int index) const
  QMetaMethod::MethodType methodType(int index) const override {
    if (taken[17]) {
      int handled = 0;
      CuteSourceApiMapCall17 call = reinterpret_cast<CuteSourceApiMapCall17>(taken[17]);
      int given = call(this, index, &handled);
      if (handled) return static_cast<QMetaMethod::MethodType>(given);
    }
    return {};
  }

  //  const QByteArray SourceApiMap::typeName(int index) const
  const QByteArray typeName(int index) const override {
    if (taken[18]) {
      int handled = 0;
      CuteSourceApiMapCall18 call = reinterpret_cast<CuteSourceApiMapCall18>(taken[18]);
      const QByteArray * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int SourceApiMap::propertyIndexFromSignal(int index) const
  int propertyIndexFromSignal(int index) const override {
    if (taken[19]) {
      int handled = 0;
      CuteSourceApiMapCall19 call = reinterpret_cast<CuteSourceApiMapCall19>(taken[19]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int SourceApiMap::propertyRawIndexFromSignal(int index) const
  int propertyRawIndexFromSignal(int index) const override {
    if (taken[20]) {
      int handled = 0;
      CuteSourceApiMapCall20 call = reinterpret_cast<CuteSourceApiMapCall20>(taken[20]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QByteArray SourceApiMap::objectSignature() const
  QByteArray objectSignature() const override {
    if (taken[21]) {
      int handled = 0;
      CuteSourceApiMapCall21 call = reinterpret_cast<CuteSourceApiMapCall21>(taken[21]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool SourceApiMap::isDynamic() const
  bool isDynamic() const override {
    if (taken[22]) {
      int handled = 0;
      CuteSourceApiMapCall22 call = reinterpret_cast<CuteSourceApiMapCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return SourceApiMap::isDynamic();
  }

  //  bool SourceApiMap::isAdapterSignal(int a0) const
  bool isAdapterSignal(int a0) const override {
    if (taken[23]) {
      int handled = 0;
      CuteSourceApiMapCall23 call = reinterpret_cast<CuteSourceApiMapCall23>(taken[23]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return SourceApiMap::isAdapterSignal(a0);
  }

  //  bool SourceApiMap::isAdapterMethod(int a0) const
  bool isAdapterMethod(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      CuteSourceApiMapCall24 call = reinterpret_cast<CuteSourceApiMapCall24>(taken[24]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return SourceApiMap::isAdapterMethod(a0);
  }

  //  bool SourceApiMap::isAdapterProperty(int a0) const
  bool isAdapterProperty(int a0) const override {
    if (taken[25]) {
      int handled = 0;
      CuteSourceApiMapCall25 call = reinterpret_cast<CuteSourceApiMapCall25>(taken[25]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return SourceApiMap::isAdapterProperty(a0);
  }
};

//  SourceApiMap::~SourceApiMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN12SourceApiMapD1Ev(SourceApiMap *self) {
  delete self;
}

//  QString SourceApiMap::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12SourceApiMap4nameEv(const SourceApiMap *self) {
  return new QString(self->name());
}

//  QString SourceApiMap::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12SourceApiMap8typeNameEv(const SourceApiMap *self) {
  return new QString(self->typeName());
}

//  QByteArray SourceApiMap::className() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12SourceApiMap9classNameEv(const SourceApiMap *self) {
  return new QByteArray(self->className());
}

//  int SourceApiMap::enumCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap9enumCountEv(const SourceApiMap *self) {
  return self->enumCount();
}

//  int SourceApiMap::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap13propertyCountEv(const SourceApiMap *self) {
  return self->propertyCount();
}

//  int SourceApiMap::signalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap11signalCountEv(const SourceApiMap *self) {
  return self->signalCount();
}

//  int SourceApiMap::methodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap11methodCountEv(const SourceApiMap *self) {
  return self->methodCount();
}

//  int SourceApiMap::sourceEnumIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap15sourceEnumIndexEi(
    const SourceApiMap *self,
    int index) {
  return self->sourceEnumIndex(index);
}

//  int SourceApiMap::sourcePropertyIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap19sourcePropertyIndexEi(
    const SourceApiMap *self,
    int index) {
  return self->sourcePropertyIndex(index);
}

//  int SourceApiMap::sourceSignalIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap17sourceSignalIndexEi(
    const SourceApiMap *self,
    int index) {
  return self->sourceSignalIndex(index);
}

//  int SourceApiMap::sourceMethodIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap17sourceMethodIndexEi(
    const SourceApiMap *self,
    int index) {
  return self->sourceMethodIndex(index);
}

//  int SourceApiMap::signalParameterCount(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap20signalParameterCountEi(
    const SourceApiMap *self,
    int index) {
  return self->signalParameterCount(index);
}

//  int SourceApiMap::signalParameterType(int sigIndex, int paramIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap19signalParameterTypeEii(
    const SourceApiMap *self,
    int sigIndex,
    int paramIndex) {
  return self->signalParameterType(sigIndex, paramIndex);
}

//  const QByteArray SourceApiMap::signalSignature(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12SourceApiMap15signalSignatureEi(
    const SourceApiMap *self,
    int index) {
  return new QByteArray(self->signalSignature(index));
}

//  QByteArrayList SourceApiMap::signalParameterNames(int index) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK12SourceApiMap20signalParameterNamesEi(
    const SourceApiMap *self,
    int index) {
  return new QList<QByteArray>(self->signalParameterNames(index));
}

//  int SourceApiMap::methodParameterCount(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap20methodParameterCountEi(
    const SourceApiMap *self,
    int index) {
  return self->methodParameterCount(index);
}

//  int SourceApiMap::methodParameterType(int methodIndex, int paramIndex)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap19methodParameterTypeEii(
    const SourceApiMap *self,
    int methodIndex,
    int paramIndex) {
  return self->methodParameterType(methodIndex, paramIndex);
}

//  const QByteArray SourceApiMap::methodSignature(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12SourceApiMap15methodSignatureEi(
    const SourceApiMap *self,
    int index) {
  return new QByteArray(self->methodSignature(index));
}

//  QMetaMethod::MethodType SourceApiMap::methodType(int index) const
extern "C" Q_DECL_EXPORT
QMetaMethod::MethodType ritual_ZNK12SourceApiMap10methodTypeEi(
    const SourceApiMap *self,
    int index) {
  return self->methodType(index);
}

//  const QByteArray SourceApiMap::typeName(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12SourceApiMap8typeNameEi(
    const SourceApiMap *self,
    int index) {
  return new QByteArray(self->typeName(index));
}

//  QByteArrayList SourceApiMap::methodParameterNames(int index) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK12SourceApiMap20methodParameterNamesEi(
    const SourceApiMap *self,
    int index) {
  return new QList<QByteArray>(self->methodParameterNames(index));
}

//  int SourceApiMap::propertyIndexFromSignal(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap23propertyIndexFromSignalEi(
    const SourceApiMap *self,
    int index) {
  return self->propertyIndexFromSignal(index);
}

//  int SourceApiMap::propertyRawIndexFromSignal(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12SourceApiMap26propertyRawIndexFromSignalEi(
    const SourceApiMap *self,
    int index) {
  return self->propertyRawIndexFromSignal(index);
}

//  QByteArray SourceApiMap::objectSignature() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12SourceApiMap15objectSignatureEv(
    const SourceApiMap *self) {
  return new QByteArray(self->objectSignature());
}

//  bool SourceApiMap::isDynamic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12SourceApiMap9isDynamicEv(const SourceApiMap *self) {
  return self->isDynamic();
}

//  bool SourceApiMap::isAdapterSignal(int a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12SourceApiMap15isAdapterSignalEi(
    const SourceApiMap *self,
    int a0) {
  return self->isAdapterSignal(a0);
}

//  bool SourceApiMap::isAdapterMethod(int a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12SourceApiMap15isAdapterMethodEi(
    const SourceApiMap *self,
    int a0) {
  return self->isAdapterMethod(a0);
}

//  bool SourceApiMap::isAdapterProperty(int a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12SourceApiMap17isAdapterPropertyEi(
    const SourceApiMap *self,
    int a0) {
  return self->isAdapterProperty(a0);
}

//  a Python function taken by a CuteSourceApiMap, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SourceApiMap(
    SourceApiMap *self,
    const char *key,
    void *call) {
  return static_cast<CuteSourceApiMap *>(self)->take(key, call);
}

//  QByteArray SourceApiMap::className() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK12SourceApiMap9classNameEv(
    const SourceApiMap *self) {
  return new QByteArray(self->SourceApiMap::className());
}

//  bool SourceApiMap::isDynamic() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12SourceApiMap9isDynamicEv(const SourceApiMap *self) {
  return self->SourceApiMap::isDynamic();
}

//  bool SourceApiMap::isAdapterSignal(int a0) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12SourceApiMap15isAdapterSignalEi(
    const SourceApiMap *self,
    int a0) {
  return self->SourceApiMap::isAdapterSignal(a0);
}

//  bool SourceApiMap::isAdapterMethod(int a0) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12SourceApiMap15isAdapterMethodEi(
    const SourceApiMap *self,
    int a0) {
  return self->SourceApiMap::isAdapterMethod(a0);
}

//  bool SourceApiMap::isAdapterProperty(int a0) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12SourceApiMap17isAdapterPropertyEi(
    const SourceApiMap *self,
    int a0) {
  return self->SourceApiMap::isAdapterProperty(a0);
}

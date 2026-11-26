//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qshaderprogrambuilder.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DRender/qshaderprogrambuilder.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DRender::QShaderProgramBuilder that Python can take functions over in. Every Qt3DRender::QShaderProgramBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QShaderProgramBuilderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QShaderProgramBuilderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramBuilderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramBuilderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramBuilderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramBuilderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderProgramBuilderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QShaderProgramBuilder : public Qt3DRender::QShaderProgramBuilder {
public:
  using Qt3DRender::QShaderProgramBuilder::QShaderProgramBuilder;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QShaderProgramBuilderCall0 call = reinterpret_cast<CuteQt3DRender_QShaderProgramBuilderCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QShaderProgramBuilderCall1 call = reinterpret_cast<CuteQt3DRender_QShaderProgramBuilderCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QShaderProgramBuilderCall2 call = reinterpret_cast<CuteQt3DRender_QShaderProgramBuilderCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_QShaderProgramBuilderCall3 call = reinterpret_cast<CuteQt3DRender_QShaderProgramBuilderCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_QShaderProgramBuilderCall4 call = reinterpret_cast<CuteQt3DRender_QShaderProgramBuilderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_QShaderProgramBuilderCall5 call = reinterpret_cast<CuteQt3DRender_QShaderProgramBuilderCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_QShaderProgramBuilderCall6 call = reinterpret_cast<CuteQt3DRender_QShaderProgramBuilderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QShaderProgramBuilder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender21QShaderProgramBuilder10metaObjectEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QShaderProgramBuilder::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender21QShaderProgramBuilder11qt_metacastEPKc(
    Qt3DRender::QShaderProgramBuilder *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QShaderProgramBuilder::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender21QShaderProgramBuilder11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QShaderProgramBuilder *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QShaderProgramBuilder::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender21QShaderProgramBuilder2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QShaderProgramBuilder::tr(s, c, n));
}

//  Qt3DRender::QShaderProgramBuilder::QShaderProgramBuilder(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgramBuilder *ritual_ZN10Qt3DRender21QShaderProgramBuilderC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QShaderProgramBuilder(parent);
}

//  Qt3DRender::QShaderProgramBuilder::~QShaderProgramBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilderD1Ev(
    Qt3DRender::QShaderProgramBuilder *self) {
  delete self;
}

//  QShaderProgram *Qt3DRender::QShaderProgramBuilder::shaderProgram() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgram *ritual_ZNK10Qt3DRender21QShaderProgramBuilder13shaderProgramEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return self->shaderProgram();
}

//  QStringList Qt3DRender::QShaderProgramBuilder::enabledLayers() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender21QShaderProgramBuilder13enabledLayersEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QList<QString>(self->enabledLayers());
}

//  QUrl Qt3DRender::QShaderProgramBuilder::vertexShaderGraph() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender21QShaderProgramBuilder17vertexShaderGraphEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QUrl(self->vertexShaderGraph());
}

//  QUrl Qt3DRender::QShaderProgramBuilder::tessellationControlShaderGraph()
//      const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender21QShaderProgramBuilder30tessellationControlShaderGraphEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QUrl(self->tessellationControlShaderGraph());
}

//  QUrl
//      Qt3DRender::QShaderProgramBuilder::tessellationEvaluationShaderGraph(
//      ) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender21QShaderProgramBuilder33tessellationEvaluationShaderGraphEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QUrl(self->tessellationEvaluationShaderGraph());
}

//  QUrl Qt3DRender::QShaderProgramBuilder::geometryShaderGraph() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender21QShaderProgramBuilder19geometryShaderGraphEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QUrl(self->geometryShaderGraph());
}

//  QUrl Qt3DRender::QShaderProgramBuilder::fragmentShaderGraph() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender21QShaderProgramBuilder19fragmentShaderGraphEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QUrl(self->fragmentShaderGraph());
}

//  QUrl Qt3DRender::QShaderProgramBuilder::computeShaderGraph() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender21QShaderProgramBuilder18computeShaderGraphEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QUrl(self->computeShaderGraph());
}

//  QByteArray Qt3DRender::QShaderProgramBuilder::vertexShaderCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender21QShaderProgramBuilder16vertexShaderCodeEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QByteArray(self->vertexShaderCode());
}

//  QByteArray
//      Qt3DRender::QShaderProgramBuilder::tessellationControlShaderCode()
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender21QShaderProgramBuilder29tessellationControlShaderCodeEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QByteArray(self->tessellationControlShaderCode());
}

//  QByteArray
//      Qt3DRender::QShaderProgramBuilder::tessellationEvaluationShaderCode()
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender21QShaderProgramBuilder32tessellationEvaluationShaderCodeEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QByteArray(self->tessellationEvaluationShaderCode());
}

//  QByteArray Qt3DRender::QShaderProgramBuilder::geometryShaderCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender21QShaderProgramBuilder18geometryShaderCodeEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QByteArray(self->geometryShaderCode());
}

//  QByteArray Qt3DRender::QShaderProgramBuilder::fragmentShaderCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender21QShaderProgramBuilder18fragmentShaderCodeEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QByteArray(self->fragmentShaderCode());
}

//  QByteArray Qt3DRender::QShaderProgramBuilder::computeShaderCode() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10Qt3DRender21QShaderProgramBuilder17computeShaderCodeEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return new QByteArray(self->computeShaderCode());
}

//  void Qt3DRender::QShaderProgramBuilder::setShaderProgram(Qt3DRender::QSha
//      derProgram *program)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder16setShaderProgramEPNS_14QShaderProgramE(
    Qt3DRender::QShaderProgramBuilder *self,
    Qt3DRender::QShaderProgram *program) {
  self->setShaderProgram(program);
}

//  void Qt3DRender::QShaderProgramBuilder::setEnabledLayers(const
//      QStringList &layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder16setEnabledLayersERK5QListI7QStringE(
    Qt3DRender::QShaderProgramBuilder *self,
    const QList<QString> *layers) {
  self->setEnabledLayers(*layers);
}

//  void Qt3DRender::QShaderProgramBuilder::setVertexShaderGraph(const QUrl
//      &vertexShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder20setVertexShaderGraphERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *vertexShaderGraph) {
  self->setVertexShaderGraph(*vertexShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::setTessellationControlShaderGraph
//      (const QUrl &tessellationControlShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder33setTessellationControlShaderGraphERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *tessellationControlShaderGraph) {
  self->setTessellationControlShaderGraph(*tessellationControlShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::setTessellationEvaluationShaderGr
//      aph(const QUrl &tessellationEvaluationShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder36setTessellationEvaluationShaderGraphERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *tessellationEvaluationShaderGraph) {
  self->setTessellationEvaluationShaderGraph(
      *tessellationEvaluationShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::setGeometryShaderGraph(const QUrl
//      &geometryShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder22setGeometryShaderGraphERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *geometryShaderGraph) {
  self->setGeometryShaderGraph(*geometryShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::setFragmentShaderGraph(const QUrl
//      &fragmentShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder22setFragmentShaderGraphERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *fragmentShaderGraph) {
  self->setFragmentShaderGraph(*fragmentShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::setComputeShaderGraph(const QUrl
//      &computeShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder21setComputeShaderGraphERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *computeShaderGraph) {
  self->setComputeShaderGraph(*computeShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::shaderProgramChanged(Qt3DRender::
//      QShaderProgram *shaderProgram)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder20shaderProgramChangedEPNS_14QShaderProgramE(
    Qt3DRender::QShaderProgramBuilder *self,
    Qt3DRender::QShaderProgram *shaderProgram) {
  self->shaderProgramChanged(shaderProgram);
}

//  void Qt3DRender::QShaderProgramBuilder::enabledLayersChanged(const
//      QStringList &layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder20enabledLayersChangedERK5QListI7QStringE(
    Qt3DRender::QShaderProgramBuilder *self,
    const QList<QString> *layers) {
  self->enabledLayersChanged(*layers);
}

//  void Qt3DRender::QShaderProgramBuilder::vertexShaderGraphChanged(const
//      QUrl &vertexShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder24vertexShaderGraphChangedERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *vertexShaderGraph) {
  self->vertexShaderGraphChanged(*vertexShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::tessellationControlShaderGraphCha
//      nged(const QUrl &tessellationControlShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder37tessellationControlShaderGraphChangedERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *tessellationControlShaderGraph) {
  self->tessellationControlShaderGraphChanged(
      *tessellationControlShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::tessellationEvaluationShaderGraph
//      Changed(const QUrl &tessellationEvaluationShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder40tessellationEvaluationShaderGraphChangedERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *tessellationEvaluationShaderGraph) {
  self->tessellationEvaluationShaderGraphChanged(
      *tessellationEvaluationShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::geometryShaderGraphChanged(const
//      QUrl &geometryShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder26geometryShaderGraphChangedERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *geometryShaderGraph) {
  self->geometryShaderGraphChanged(*geometryShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::fragmentShaderGraphChanged(const
//      QUrl &fragmentShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder26fragmentShaderGraphChangedERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *fragmentShaderGraph) {
  self->fragmentShaderGraphChanged(*fragmentShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::computeShaderGraphChanged(const
//      QUrl &computeShaderGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder25computeShaderGraphChangedERK4QUrl(
    Qt3DRender::QShaderProgramBuilder *self,
    const QUrl *computeShaderGraph) {
  self->computeShaderGraphChanged(*computeShaderGraph);
}

//  void Qt3DRender::QShaderProgramBuilder::vertexShaderCodeChanged(const
//      QByteArray &vertexShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder23vertexShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgramBuilder *self,
    const QByteArray *vertexShaderCode) {
  self->vertexShaderCodeChanged(*vertexShaderCode);
}

//  void Qt3DRender::QShaderProgramBuilder::tessellationControlShaderCodeChan
//      ged(const QByteArray &tessellationControlShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder36tessellationControlShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgramBuilder *self,
    const QByteArray *tessellationControlShaderCode) {
  self->tessellationControlShaderCodeChanged(*tessellationControlShaderCode);
}

//  void Qt3DRender::QShaderProgramBuilder::tessellationEvaluationShaderCodeC
//      hanged(const QByteArray &tessellationEvaluationShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder39tessellationEvaluationShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgramBuilder *self,
    const QByteArray *tessellationEvaluationShaderCode) {
  self->tessellationEvaluationShaderCodeChanged(
      *tessellationEvaluationShaderCode);
}

//  void Qt3DRender::QShaderProgramBuilder::geometryShaderCodeChanged(const
//      QByteArray &geometryShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder25geometryShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgramBuilder *self,
    const QByteArray *geometryShaderCode) {
  self->geometryShaderCodeChanged(*geometryShaderCode);
}

//  void Qt3DRender::QShaderProgramBuilder::fragmentShaderCodeChanged(const
//      QByteArray &fragmentShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder25fragmentShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgramBuilder *self,
    const QByteArray *fragmentShaderCode) {
  self->fragmentShaderCodeChanged(*fragmentShaderCode);
}

//  void Qt3DRender::QShaderProgramBuilder::computeShaderCodeChanged(const
//      QByteArray &computeShaderCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QShaderProgramBuilder24computeShaderCodeChangedERK10QByteArray(
    Qt3DRender::QShaderProgramBuilder *self,
    const QByteArray *computeShaderCode) {
  self->computeShaderCodeChanged(*computeShaderCode);
}

//  Qt3DRender::QShaderProgramBuilder::QShaderProgramBuilder(QShaderProgramBu
//      ilderPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgramBuilder *ritual_ZN10Qt3DRender21QShaderProgramBuilderC1ERNS_28QShaderProgramBuilderPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QShaderProgramBuilderPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QShaderProgramBuilder(*dd, parent);
}

//  QShaderProgramBuilderPrivate *Qt3DRender::QShaderProgramBuilder::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderProgramBuilderPrivate *ritual_ZN10Qt3DRender21QShaderProgramBuilder6d_funcEv(
    Qt3DRender::QShaderProgramBuilder *self) {
  return self->d_func();
}

//  const QShaderProgramBuilderPrivate
//      *Qt3DRender::QShaderProgramBuilder::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QShaderProgramBuilderPrivate *ritual_ZNK10Qt3DRender21QShaderProgramBuilder6d_funcEv(
    const Qt3DRender::QShaderProgramBuilder *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QShaderProgramBuilder, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QShaderProgramBuilder(
    Qt3DRender::QShaderProgramBuilder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QShaderProgramBuilder *>(self)->take(key, call);
}

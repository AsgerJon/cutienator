//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/qsvggenerator.h, Qt 6.12.0. Changes made here are lost.
#include <QtSvg/qtsvgglobal.h>
#if !defined(QT_NO_SVGGENERATOR)
#include <QtSvg/qsvggenerator.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  Only a class built on QSvgGenerator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSvgGenerator : QSvgGenerator {
  using QSvgGenerator::paintEngine;
  using QSvgGenerator::metric;
  using QSvgGenerator::initPainter;
};

//  A QSvgGenerator that Python can take functions over in. Every QSvgGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SVGGENERATOR)
typedef void * (*CuteQSvgGeneratorCall0)(const void *, int *);
#endif  // !defined(QT_NO_SVGGENERATOR)
#if !defined(QT_NO_SVGGENERATOR)
typedef int (*CuteQSvgGeneratorCall1)(const void *, int, int *);
#endif  // !defined(QT_NO_SVGGENERATOR)
#if !defined(QT_NO_SVGGENERATOR)
typedef void (*CuteQSvgGeneratorCall2)(const void *, QPainter *, int *);
#endif  // !defined(QT_NO_SVGGENERATOR)
typedef int (*CuteQSvgGeneratorCall3)(const void *, int *);
typedef void * (*CuteQSvgGeneratorCall4)(const void *, QPoint *, int *);
typedef void * (*CuteQSvgGeneratorCall5)(const void *, int *);
class CuteQSvgGenerator : public QSvgGenerator {
public:
  using QSvgGenerator::QSvgGenerator;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SVGGENERATOR)
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SVGGENERATOR)
#if !defined(QT_NO_SVGGENERATOR)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_SVGGENERATOR)
#if !defined(QT_NO_SVGGENERATOR)
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_SVGGENERATOR)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_SVGGENERATOR)
  //  QPaintEngine *QSvgGenerator::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgGeneratorCall0 call = reinterpret_cast<CuteQSvgGeneratorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QSvgGenerator::paintEngine();
  }
#endif  // !defined(QT_NO_SVGGENERATOR)

#if !defined(QT_NO_SVGGENERATOR)
  //  int QSvgGenerator::metric(QPaintDevice::PaintDeviceMetric metric)
  //      const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgGeneratorCall1 call = reinterpret_cast<CuteQSvgGeneratorCall1>(taken[1]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QSvgGenerator::metric(metric);
  }
#endif  // !defined(QT_NO_SVGGENERATOR)

#if !defined(QT_NO_SVGGENERATOR)
  //  void QSvgGenerator::initPainter(QPainter *a0) const
  void initPainter(QPainter *a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgGeneratorCall2 call = reinterpret_cast<CuteQSvgGeneratorCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSvgGenerator::initPainter(a0);
  }
#endif  // !defined(QT_NO_SVGGENERATOR)

  //  int QPaintDevice::devType() const
  int devType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgGeneratorCall3 call = reinterpret_cast<CuteQSvgGeneratorCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintDevice::devType();
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSvgGeneratorCall4 call = reinterpret_cast<CuteQSvgGeneratorCall4>(taken[4]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSvgGeneratorCall5 call = reinterpret_cast<CuteQSvgGeneratorCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  QSvgGenerator::QSvgGenerator()
extern "C" Q_DECL_EXPORT
QSvgGenerator *ritual_ZN13QSvgGeneratorC1Ev() {
  return new CuteQSvgGenerator();
}

//  QSvgGenerator::QSvgGenerator(SvgVersion version)
extern "C" Q_DECL_EXPORT
QSvgGenerator *ritual_ZN13QSvgGeneratorC1ENS_10SvgVersionE(
    QSvgGenerator::SvgVersion version) {
  return new CuteQSvgGenerator(version);
}

//  QSvgGenerator::~QSvgGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGeneratorD1Ev(QSvgGenerator *self) {
  delete self;
}

//  QString QSvgGenerator::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSvgGenerator5titleEv(const QSvgGenerator *self) {
  return new QString(self->title());
}

//  void QSvgGenerator::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGenerator8setTitleERK7QString(
    QSvgGenerator *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QString QSvgGenerator::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSvgGenerator11descriptionEv(
    const QSvgGenerator *self) {
  return new QString(self->description());
}

//  void QSvgGenerator::setDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGenerator14setDescriptionERK7QString(
    QSvgGenerator *self,
    const QString *description) {
  self->setDescription(*description);
}

//  QSize QSvgGenerator::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QSvgGenerator4sizeEv(const QSvgGenerator *self) {
  return new QSize(self->size());
}

//  void QSvgGenerator::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGenerator7setSizeERK5QSize(
    QSvgGenerator *self,
    const QSize *size) {
  self->setSize(*size);
}

//  QRect QSvgGenerator::viewBox() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QSvgGenerator7viewBoxEv(const QSvgGenerator *self) {
  return new QRect(self->viewBox());
}

//  QRectF QSvgGenerator::viewBoxF() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QSvgGenerator8viewBoxFEv(const QSvgGenerator *self) {
  return new QRectF(self->viewBoxF());
}

//  void QSvgGenerator::setViewBox(const QRect &viewBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGenerator10setViewBoxERK5QRect(
    QSvgGenerator *self,
    const QRect *viewBox) {
  self->setViewBox(*viewBox);
}

//  void QSvgGenerator::setViewBox(const QRectF &viewBox)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGenerator10setViewBoxERK6QRectF(
    QSvgGenerator *self,
    const QRectF *viewBox) {
  self->setViewBox(*viewBox);
}

//  QString QSvgGenerator::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSvgGenerator8fileNameEv(const QSvgGenerator *self) {
  return new QString(self->fileName());
}

//  void QSvgGenerator::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGenerator11setFileNameERK7QString(
    QSvgGenerator *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QIODevice *QSvgGenerator::outputDevice() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK13QSvgGenerator12outputDeviceEv(
    const QSvgGenerator *self) {
  return self->outputDevice();
}

//  void QSvgGenerator::setOutputDevice(QIODevice *outputDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGenerator15setOutputDeviceEP9QIODevice(
    QSvgGenerator *self,
    QIODevice *outputDevice) {
  self->setOutputDevice(outputDevice);
}

//  void QSvgGenerator::setResolution(int dpi)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgGenerator13setResolutionEi(
    QSvgGenerator *self,
    int dpi) {
  self->setResolution(dpi);
}

//  int QSvgGenerator::resolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QSvgGenerator10resolutionEv(const QSvgGenerator *self) {
  return self->resolution();
}

//  SvgVersion QSvgGenerator::svgVersion() const
extern "C" Q_DECL_EXPORT
QSvgGenerator::SvgVersion ritual_ZNK13QSvgGenerator10svgVersionEv(
    const QSvgGenerator *self) {
  return self->svgVersion();
}

//  QPaintEngine *QSvgGenerator::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK13QSvgGenerator11paintEngineEv(
    const QSvgGenerator *self) {
  return self->paintEngine();
}

//  int QSvgGenerator::metric(QPaintDevice::PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QSvgGenerator6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QSvgGenerator *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return self->metric(metric);
}

//  void QSvgGenerator::initPainter(QPainter *a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QSvgGenerator11initPainterEP8QPainter(
    const QSvgGenerator *self,
    QPainter *a0) {
  self->initPainter(a0);
}

//  a Python function taken by a CuteQSvgGenerator, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgGenerator(
    QSvgGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgGenerator *>(self)->take(key, call);
}

//  QPaintEngine *QSvgGenerator::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK13QSvgGenerator11paintEngineEv(
    const QSvgGenerator *self) {
  return static_cast<const OwnQSvgGenerator *>(self)->OwnQSvgGenerator::paintEngine();
}

//  int QSvgGenerator::metric(QPaintDevice::PaintDeviceMetric metric) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QSvgGenerator6metricEN12QPaintDevice17PaintDeviceMetricE(
    const QSvgGenerator *self,
    QPaintDevice::PaintDeviceMetric metric) {
  return static_cast<const OwnQSvgGenerator *>(self)->OwnQSvgGenerator::metric(
      metric);
}

//  void QSvgGenerator::initPainter(QPainter *a0) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK13QSvgGenerator11initPainterEP8QPainter(
    const QSvgGenerator *self,
    QPainter *a0) {
  static_cast<const OwnQSvgGenerator *>(self)->OwnQSvgGenerator::initPainter(
      a0);
}

#endif  // !defined(QT_NO_SVGGENERATOR)
